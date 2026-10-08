"""Автопроверка промпта по формальным признакам ТЗ 03. Аргументы: путь к prompt.md, путь к TZ.md, режим (DEEP|SHALLOW)."""
import re, sys
p, tz, mode = sys.argv[1], sys.argv[2], sys.argv[3]
t = open(p, encoding='utf-8').read()
z = open(tz, encoding='utf-8').read()
lock = re.search(r"^> (Photorealistic, an unretouched real photograph[^\n]*)$", z, re.M).group(1).strip()
start = t.find("Photorealistic")
body = t[start:].strip() if start >= 0 else t.strip()
main = body[:body.rfind(lock)] if lock in body else body
res = []
def chk(name, ok, note=""):
    res.append((ok, name, note))
chk("начинается с Photorealistic", start >= 0 and t[start:start+14] == "Photorealistic" and not re.search(r"[A-Za-z]", t[:start].split('\n')[-1] if start>0 else ""))
chk("Realism Lock v3 дословно и последним", body.endswith(lock), "" if body.endswith(lock) else "нет/не последний")
chk("длина ≤ ~6000 символов", len(body) <= 6000, f"{len(body)} симв.")
if mode == "PHONE":
    chk("якорь телефона в стандартном режиме", bool(re.search(r"standard photo mode", main, re.I)) and bool(re.search(r"iPhone|smartphone", main, re.I)))
    chk("кто снимает", bool(re.search(r"taken by|held by|selfie|on a tripod", main, re.I)))
    chk("конкретное время", bool(re.search(r"\b\d{1,2}(:\d\d)?\s?(am|pm|a\.m\.|p\.m\.)", main, re.I)))
    soft = re.findall(r"\b(soft(?:er|ened|ly blurred)?|blur(?:red|ry)?|defocus\w*|out of focus)\b", main, re.I)
    soft = [w for w in soft if w.lower()!="soft"] + [m for m in re.findall(r"\bsoft\b(?! light| shadow| edge| fill)", main, re.I)]
    bg_sents=[x for x in re.split(r"(?<=[.;])\s", main) if not re.search(r"foreground|close to the lens|near the lens", x, re.I)]
    soft=re.findall(r"\b(soft(?:er|ened)?|blur(?:red|ry)?|out of focus)\b(?! light| shadow| edge| fill)", " ".join(bg_sents), re.I)
    chk("нет слов мягкости для фона", not soft, ", ".join(soft))
    chk("фон ясно узнаваем (recognisable/readable)", bool(re.search(r"recogni[sz]able|clearly readable", main, re.I)))
    chk("нет f/11 и deep depth of field", not re.search(r"f/11|deep depth of field", main, re.I))
    chk("нет (no|not) portrait mode и чужих миллиметров", not re.search(r"\b(no|not) portrait mode", main, re.I) and all(m in ("24","26") for m in re.findall(r"(\d+)\s?mm", main)))
elif mode == "DEEP":
    chk("deep depth of field", "deep depth of field" in main.lower())
    chk("якорь объектива/телефона", bool(re.search(r"\d+\s?mm[- ]equivalent|smartphone main camera", main, re.I)) and (bool(re.search(r"f/\d", main)) or "smartphone" in main.lower()))
    soft = re.findall(r"\b(soft\w*|blur\w*|defocus\w*|bokeh|out of focus)\b", main, re.I)
    chk("нет слов мягкости в основном тексте", not soft, ", ".join(soft))
    chk("явное in focus / crisp", bool(re.search(r"\bin focus\b|\bcrisp\b", main, re.I)))
else:
    chk("shallow depth of field / bokeh задан", bool(re.search(r"shallow depth of field|bokeh|out of focus", main, re.I)))
    chk("якорь объектива/портретного режима", bool(re.search(r"\d+\s?mm|portrait mode|f/\d", main, re.I)))
chk("нет avatar / character card в тексте", not re.search(r"avatar|character card|digital human|\bCGI\b", main, re.I))
chk("референсы по порядку image 1 / image 2", bool(re.search(r"image 1", main, re.I) and re.search(r"image 2", main, re.I)))
chk("исключены футболка и цепочка с референсов", bool(re.search(r"blue-grey T-shirt|blue-gray T-shirt", main, re.I)) and bool(re.search(r"chain|necklace", main, re.I)))
chk("тон кожи назван словами", bool(re.search(r"\b(fair|light|olive|pale)[\w -]{0,20}skin|skin (is|tone is)[\w -]{0,10}\b(fair|light|olive|pale)", main, re.I)))
chk("нейтральный баланс белого", bool(re.search(r"neutral[\w -]{0,25}white balance|auto white balance|5[0-9]00\s?K", main, re.I)))
g = len(re.findall(r"\bgolden\b", main, re.I))
chk("golden не больше 1 раза", g <= 1, f"golden×{g}")
chk("нет just above the horizon / golden hour / no portrait mode", not re.search(r"just above the horizon|golden hour|no portrait mode", main, re.I))
day = not re.search(r"evening|night|dusk|after sunset|dark", main, re.I)
if day: chk("нет зерна/шума на дневном снимке", not re.search(r"\bgrain\b|\bnoise\b", main, re.I))
chk("есть передний план", bool(re.search(r"foreground", main, re.I)))
chk("нет студийных слов", not re.search(r"\b(studio|flawless|perfect skin|8K|masterpiece|ultra-detailed)\b", main, re.I))
if any(re.search(r"\bsun\b", x, re.I) and re.search(r"out of frame|outside the frame|off-frame", x, re.I) for x in re.split(r"(?<=[.;])\s", main)):
    chk("солнце вне кадра → небо без диска", bool(re.search(r"sunless|no sun disc", main, re.I)))
bad = [r for r in res if not r[0]]
for ok, n, note in res:
    print(("✅ " if ok else "❌ ") + n + (f" — {note}" if note else ""))
print(f"ИТОГО: {len(res)-len(bad)}/{len(res)}")
