# Прогон 2 — по исправленным ТЗ (02 v6.3 → 03 v6.5)

## Шаг 1. ОПИСАНИЕ ИЗОБРАЖЕНИЯ СЦЕНЫ — s01 (по ТЗ 02 v6.3)

Блоки, изменившиеся по сравнению с прогоном 1, отмечены знаком ✱.

**1. INTENT / IMAGE TYPE.** Естественная фотография на натуре: автор на открытом горном хребте на рассвете. Впечатление — спокойная уверенность, начало пути. Первым зритель видит лицо и прямой взгляд, затем — простор гор, которые должны читаться как реальное место. Верхняя треть — чистое небо под заголовок.

**2. PRIMARY SUBJECT.** Один человек — принятый ИИ-аватар автора (карта v1.1); лицо и голова — HEAD_GRID, телосложение — BODY_GRID. Горы — поддерживающий фон, не второй центр внимания.

**3. ACTION / STATE.** Стоит неподвижно, смотрит прямо в объектив. Спокойная полуулыбка с закрытым ртом: уголки губ чуть приподняты, щёки слегка подняты без прищура, брови расслаблены.

**4. SUBJECT GEOMETRY.** Корпус почти фронтально, чуть повёрнут к правому краю кадра; плечи ровные. Голова почти фронтально. Руки свободно опущены, кисти ниже нижнего края.

**5. SPATIAL.** ✱ Камера (~1,3 м) → человек → слева по кадру хребет уходит вниз (камень, лишайник, трава) → справа долина с дымкой → дальние хребты на уровне плеч; голова частично на фоне дальних склонов, частично на фоне неба.

**6. ENVIRONMENT.** Открытый горный хребет без снега, рассвет, ясно, слоистая дымка в долине. Серый камень, лишайник, низкая трава в росе.

**7. CAMERA.** ✱ Обычная камера, широкий угол (около 28 мм в пересчёте на полный кадр), примерно 1,3 м от человека, на высоте груди, чуть снизу вверх; горизонт низко. **Режим резкости: всё в фокусе — от камней за его спиной до самого дальнего хребта.** Широкий угол и близкая камера выбраны, чтобы кадр по пояс не превратился в портрет с размытым фоном; ближе ~1 м камеру не ставить, чтобы не исказить нос.

**8. FRAMING / DEPTH.** ✱ По пояс; человек чуть левее центра, больше воздуха справа; верхняя треть — ровное небо, голова сразу под ней.
- Ближний план (камни, трава за ним): в фокусе, видны трещины камня и травинки.
- Человек: в фокусе, той же естественной чёткости, что камни рядом; лицо не резче камня и ткани.
- Средний план (склоны долины): в фокусе, различимы промоины и гребни; дымка немного снижает контраст.
- Дальний план (хребты): в фокусе, контуры чёткие; дымка делает их светлее, голубее, ниже по контрасту, мелкие детали не различимы.

**9. LIGHTING.** ✱ Низкое солнце за правым краем кадра, сбоку и чуть спереди, почти горизонтальное, рассеянное дымкой; переходы теней плавные. Правая по кадру сторона лица (висок, щека, бок носа) тёплая и светлая; переход по спинке носа; левая половина в открытой тени от неба, глаз хорошо виден. Тёплый контур на правых волосах и ухе. Солнечных бликов объектива нет.

**10. MATERIALS.** Тёмно-графитовая матовая ветровка, застёгнута чуть ниже ключиц, видна горловина тёмно-серой футболки; без логотипов и украшений.

**11. COLOR.** Нейтральный дневной баланс белого. Освещённая кожа тёплая персиково-золотистая, теневая — чуть холоднее. Освещённые склоны розово-золотые, теневые — сине-серые. Небо — от светло-голубого к бледному персику у горизонта. Экспозиция по лицу, небо без пересвета, умеренный контраст.

**12. REFERENCE LOCKS.** HEAD_GRID → автор → голова, лицо, волосы. BODY_GRID → автор → телосложение и пропорции.

**13. OUTPUT.** Вертикаль 9:16; верхняя треть свободна.

## Шаг 2. Промпт по ТЗ 03 v6.5

**s01 — FINAL PROMPT (EN) — character card v1.1 — refs: HEAD_GRID, BODY_GRID**  
*(строка-заголовок в генератор не копируется)*

```text
Vertical 9:16 wide-angle environmental photograph with deep depth of field, 28mm-equivalent lens at f/8–f/11 focused for front-to-back sharpness: the man shown in HEAD_GRID and BODY_GRID stands on an open mountain ridge at sunrise, waist-up, looking straight into the lens with a calm closed-mouth half-smile, no squint. Torso almost frontal, turned slightly toward frame right, arms hanging loosely. Slightly left of centre, open space on the sunlit right. The top third of the frame is clear sky; his head sits just below it.

Use HEAD_GRID only for face, head and hair identity and BODY_GRID only for build and proportions; do not transfer their lighting, exposure, white balance, skin colour rendering, retouching or sharpness. Keep his narrow, vertically elongated face with lean cheeks and an angular jaw; long, narrow, strongly projecting nose; horizontally elongated eyes under straight brows set close to them. Short dark-brown side-swept hair, clean-shaven, slim build.

Camera 1.3 m away at chest height, tilted slightly up, horizon low. Frame left: grey lichen-covered rock and dewy grass. Frame right: a hazy valley and snowless rocky ranges at his shoulder height. Everything from the rocks behind him to the farthest ridgeline is in focus: rock cracks and grass blades are crisp, the middle slopes show clear gullies, and the far ranges keep crisp outlines while haze makes them progressively paler, bluer and lower in contrast. His face and jacket have the same natural sharpness as the rocks beside him.

Low, haze-diffused sun just out of frame right and slightly in front of him warms his frame-right temple, cheek and nose side; the transition runs along the nose bridge; the frame-left half is in gentle open shade, eye clearly visible. Warm rim on frame-right hair and ear. Sun-facing slopes rose-gold, shaded slopes blue-grey. No lens flare.

Dark graphite matte windbreaker zipped to below the collarbones over a dark-grey T-shirt; no logos. Neutral daylight white balance: lit skin warm peach-gold, shaded skin slightly cooler; sky light blue to pale peach at the horizon; exposed for the face, sky unclipped, moderate contrast. No other people or text.

Authentic photorealism, a real photograph rather than a render: realistic skin, hair and material texture at the same natural level of detail as everything else at that distance, true-to-life colours, believable exposure, depth of field exactly as described above with no extra background blur, natural body language, lived-in details, no glamour retouching, no beauty filter, no oversharpening, no cutout look, no cinematic colour grading, no hyper-polished AI look.
```

## Шаг 3. Проверка по новым стоп-критериям ТЗ 03 v6.5

| Критерий | Результат |
|---|---|
| Тип снимка и режим резкости в первом предложении | ✅ `wide-angle environmental photograph with deep depth of field` |
| Технический якорь | ✅ `28mm-equivalent lens at f/8–f/11` |
| Дальний план явно «в фокусе» с конкретными деталями | ✅ `in focus`, `crisp outlines`, `clear gullies`, `rock cracks and grass blades are crisp` |
| Нет слов мягкости/размытия для фона | ✅ 0 (было 5) |
| Резкость человека не выделена отдельно | ✅ `same natural sharpness as the rocks beside him` вместо `He is fully sharp` |
| Дистанция согласована с режимом | ✅ 1,3 м + широкий угол вместо 2 м без объектива |
| Нет `AI avatar` / `character card` в тексте | ✅ ID вынесен в заголовок |
| Основной текст ≤ ~350 слов, identity-блок ≤ ~70 | ✅ 343 и 65 |
| Последний абзац — Realism Lock v2 дословно | ✅ |

## Сравнение s01 и прогона 2

| Показатель | s01 (старые ТЗ) | Прогон 2 (новые ТЗ) |
|---|---|---|
| Слов всего / основной текст | 613 / 527 | 411 / 343 |
| Слова мягкости в основном тексте | 5 (`softer`, `softened` ×2, `soft` ×2) + `subtle softness` в Realism Lock | 0 |
| Фразы «в фокусе / чётко» | 0 | 4 |
| Объектив и диафрагма | нет | 28 мм, f/8–f/11 |
| Отдельное «человек полностью резкий» | есть | нет — общая резкость с камнями |
| Служебные слова `AI avatar (character card v1.1)` | есть | нет |
| Конфликты Realism Lock со сценой | 5 (`candid and unposed` ↔ взгляд в камеру; `muted` ↔ розово-золотые склоны; `low contrast` ↔ `moderate contrast`; `subtle softness` ↔ резкие горы; `imperfect composition` ↔ точная композиция) | 0 |

**Чего этот тест не доказывает.** Я проверил только текст: что ТЗ теперь приводит к правильным формулировкам. Как генератор нарисует картинку, отсюда не проверить — нужно сгенерировать s01 по новому промпту у вас и сравнить с прежним результатом.
