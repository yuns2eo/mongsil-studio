# MONGSIL — CHARACTER IDENTITY LOCK

## 0. Purpose and priority

This is the identity lock for every MONGSIL image. It fixes the character’s anatomy, markings, and approved palette; pose, expression, props, costume, camera, and environment may change only when they do not alter that identity.

When sources disagree, apply this order:

1. Approved 3D turnaround references: front, 45°, profile, back, and approved detail images
2. This lock file
3. The applicable style guide
4. A scene prompt

Do not replace a visual reference with a guessed measurement, named shape, or inferred colour. If a requested view exposes a detail not visible in the supplied references, preserve the visible structure and request/reference the missing view rather than inventing it.

## 1. Non-negotiable identity

- MONGSIL is a compact, soft, upright cat mascot with a dominant head, a short rounded torso, short rounded limbs, and no visible elongated neck.
- Keep the mascot’s compact, padded silhouette. Do not apply realistic-cat anatomy, a human body, long limbs, fingers, or a slim/tall proportion.
- The head is almost circular but **slightly wider than it is tall**. It is a broad, softly rounded horizontal oval—not a sphere, a vertically long oval, a pointed wedge, or a triangular face.
- The head-to-body relationship is defined by the approved turnaround images. Do not use an unverified numeric ratio as a generation instruction.
- The body is **chubby and round** in every scene. It never becomes slim, tall, or long-waisted, including under clothing.
- Arms and legs stay as **short and stubby** as in the approved turnaround. A raised, reaching, waving, or hugging arm keeps exactly the same short length; a pose never lengthens a limb.
- When both arms are raised (cheer / hands-up pose), they open outward in a V **away from the face**, with visible space between each arm and the head. Arms must not press against or cling to the sides of the face.

### Reaching a prop without lengthening an arm

MONGSIL's arms are too short to reach many props. When a pose needs more reach, buy it from the **body**, never from the arm:

- Raise the heels and stand on **tiptoe**, lean the torso forward, bend at the hip, stretch upward through the shoulders, or move MONGSIL physically closer to the prop.
- Lower or move the prop so it falls inside the arm's real reach.
- **Reject and regenerate** any result where the forearm or upper arm is visibly longer or thinner than the turnaround, even if the pose otherwise reads correctly. A stretched arm is an identity failure, not a pose choice.

## 2. Head and face — highest-priority shape lock

### All views

- Maintain a broad forehead, full cheeks, and a soft, substantial lower face.
- Keep the facial features small and balanced within the broad rounded head; preserve their locations from the relevant approved view.
- Facial expression may change, but the underlying head volume, feature scale, and feature spacing must remain recognisably MONGSIL.

### Profile / rotation rule

When MONGSIL turns to profile or near-profile, rotate the same broad head volume; do not compress or carve away the lower face.

**Reject and regenerate** if the jaw/chin is sharply tapered, the lower face is crushed inward, or the overall profile becomes triangular. The profile must retain rounded cheek and chin volume, with an almost-round, slightly horizontally wide head silhouette.

### Mouth

- The default mouth is a **small closed curved line**. An open mouth is allowed only when the user asks for one.
- MONGSIL has **no teeth and no fangs, in any view, in any frame**. Do not draw a tooth, a fang, a tooth row, or a white highlight inside the mouth.
- In video, an open or talking mouth is the most reliable way to make teeth appear. Unless the user asked for speech, lock the mouth closed for the whole clip rather than relying on a negative prompt.

## 3. Markings and left/right orientation

All directions below use MONGSIL’s anatomical left/right. In the front view, MONGSIL’s left is the viewer’s/screen’s right. Camera movement never mirrors a marking on the body.

### Brown head / ear wave marking

- The brown marking is on MONGSIL’s anatomical left head/ear region: **screen right in the front view**.
- Its connection from the upper head/forehead area into the screen-right ear has a distinctive **wave-shaped boundary**. Treat that wave contour as an identity feature, not as a generic brown patch.
- Preserve the curve, attachment, and continuity of the wave marking through front, 45°, profile, and back views according to the relevant approved turnaround reference.
- Do not omit it, simplify it into a circle/oval/block, split it, move it to the other ear, or mirror it.

### Other markings

- Preserve the brown tail and the arm marking at their anatomical locations shown in the official reference.
- The tail silhouette is locked in **section 3-1**. Read it before writing any prompt in which the tail is visible.
- Do not add, duplicate, relocate, or mirror spots, stripes, or permanent accessories.

### Arm marking

- One small brown marking sits on the **inner edge of the upper arm on the tail side** — the body-facing edge, high up near the shoulder (screen right in the front view, the same side as the ear wave marking).
- Its shape is a **cloud cut in half vertically**: a small half-cloud attached to that edge, with two or three soft bumps along its free side. It is not a heart, circle, dot, teardrop, or stripe, and it is not a solid filled oval.
- Show it when that inner arm edge is visible and the arm hangs free. **Omit it entirely** when the arm is raised, crossed, holding a prop, or turned so the edge is hidden. Relocating it to keep it visible is a failure; leaving it out is correct.
- It stays on the upper arm edge near the shoulder. It never moves onto the waist, torso, armpit, forearm, paw, or the other arm.
- If the user asks to drop the arm marking for a specific scene or costume, follow that request for that scene and note it in the `prompts/` record. It does not change this lock.

### Body has no other markings

- Brown appears only in three places: the forehead-to-ear wave marking, the arm marking above, and the tail.
- Apart from the belly patch, the body has **no markings at all**: no brown spots on the waist, sides, back, or legs.
- This failure recurs constantly. When a prompt uses the short scene format, carry the full body-part enumeration verbatim — back, side, flank, shoulder, shoulder blade, rump, hip, waist, chest, belly, thigh, both arms, both forearms, both paws, both legs — and state that MONGSIL is **not** a calico cat with scattered patches. Shortening this block brings the stray back patch straight back.

## 3-1. Tail — shape lock

Measured against the approved 45° standing reference and the approved sitting reference. This is an identity feature and the most frequently deformed part of the character. Do not write a tail description from memory; re-read this section and the nearest reference view every time.

### Geometry

- The tail is **ONE continuous padded mass** in `#B79571`, growing from the hip on MONGSIL's anatomical left (screen right in the front view), the same side as the ear wave marking.
- In the standing 45° view it stands **UPRIGHT and is clearly TALLER THAN IT IS WIDE — roughly 1.5 to 1.8 times taller than wide.** It is never squat, never as wide as it is tall, never wider than tall.
- Its **outer edge** (facing away from the body) carries exactly **THREE rounded forms stacked vertically**: a large rounded dome at the top, then **TWO smaller rounded bumps** below it, each separated by a soft shallow notch. The top dome is the largest; the bumps do not grow going down.
- Its **inner edge** (facing the body) is **ONE long smooth unbroken curve** with **no bumps and no notches at all**. The asymmetry between the two edges is the signature of the shape.
- The **base** is a thick stalk merging smoothly into the hip. The tail never tapers to a point, never narrows to a stem, never detaches.
- The whole form reads like a **fat upright clover leaf**, or a mitten with two thumbs down one side.
- When MONGSIL sits, **the same form simply rotates** so it lies out to the side with the three rounded forms along its upper/outer edge. Rotation is allowed; reshaping is not.

### Wordings that have caused failures — do not use

Each of these has produced a deformed tail and must not appear in a prompt:

- "short and broad", "as wide as tall", "compact bunched mass" → squat blob
- "a few lobes overlapping side by side" → beads in a row
- "bumps along its free edge" without the height ratio → caterpillar
- "cloud", "fluffy", "puffy" used alone → separated puffs or a smooth paddle
- any wording that does not state **upright, taller than wide, three forms on the outer edge only, smooth inner edge**

### Mandatory verification before delivery

Crop the tail out of the result, enlarge it, and set it beside the same region of the nearest approved view. Confirm all four:

1. Height is visibly greater than width (about 1.5–1.8 : 1 standing).
2. The outer edge has a top dome plus exactly two bumps — not one, not three, not a row of equal beads.
3. The inner edge is a single smooth curve with no bumps.
4. The mass is continuous and joins the hip with a thick base.

Any failure means regenerate. Do not deliver a tail that was not compared at magnification.

## 4. Body and belly patch

- Keep the torso short, rounded, and compact beneath any clothing.
- The belly patch is centred on the belly and is a soft peach-pink **vertical oval**: its vertical dimension is slightly longer than its horizontal dimension.
- It must follow the body surface naturally. It is neither a perfect circle, a horizontal oval, a button, a pocket, nor a separate raised object.
- Preserve the reference’s placement and size relationship; do not compensate for a turned body by moving the patch off-centre.
- When clothing or a prop would cover the belly, keep at least part of the patch visible (an open vest, a short top, a prop held low) unless the user accepts it being hidden. A result where the belly patch silently disappears is a failure.

## 4-1. Paws: palm and sole pads

- Whenever a **front paw palm faces the viewer** (waving, high-five, hands-up, showing something), it has soft pink pads: one large central pad and **three** small round toe pads in an arc above it.
- Whenever a **hind paw sole is visible** (sitting, jumping, walking back foot), it has one large pad and **three** toe pads, matching the approved sitting reference.
- **Three, not four.** `Paw_Front.png`, `Paw_Hind.png` and `Sit.png` all show three. A fourth toe pad is a failure.
- The back of a paw is plain white with no pads.
- Paws stay short rounded nubs with **no separated fingers**, but a closed paw is **not a smooth blank mitten**: its free edge carries **three soft rounded toe lobes** divided by shallow grooves. Keep those lobes visible.
- Because of that, never put the bare word `fingers` in a negative prompt — it erases the toe lobes. Narrow it to `separated fingers, knuckles, claws, nails`.
- Pad pink follows the approved reference; do not assume it equals `#FFCDB4`.
- The pad count has not held reliably in generation even with the Element, an explicit number and a negative (measured failing three times). Verify at magnification in every result where a palm or sole shows, and tell the user when a video cannot be frame-checked.

## 5. Whiskers: free-standing three-dimensional structure

- Whiskers originate naturally at the cheek area and extend outward beyond the face silhouette with gentle spatial separation.
- In 3D, they must read as thin, softly curved, free-standing elements emerging from the cheek area—not printed lines, grooves, or black marks embedded flush in the face.
- Preserve the count, attachment points, length, thickness, and arrangement from the applicable approved reference. **Do not hard-code a count unless it is verified in the attached/official reference.**
- Do not make whiskers thick, rigid, facially embedded, unnaturally straight, or detached from the cheeks.

## 6. Palette lock and colour-data handling

Keep approved HEX values as literal data. Do not replace codes with colour names, delete them during revisions, or invent missing codes from a rendered screenshot.

| Element | Locked value / rule |
|---|---|
| Brown head marking, tail, and approved brown markings | `#B79571` |
| Inner ear | `#FFCDB4` |
| Black facial elements and whiskers | `#000000` |
| Belly patch, blush, paw pads, toe beans, body base | Use the existing approved palette/reference; do **not** assume they share `#FFCDB4` merely because they are pink/peach. Preserve a verified existing HEX value where supplied. |

Lighting may create material shading, but it must not redefine the base palette. White/base body colour and any unlisted pinks must be taken from the approved source rather than guessed.

## 7. Style separation

- This document defines identity, not rendering technique.
- Read `styles/MONGSIL_3D_Felt.md` for 3D material, lighting, and rendering constraints.
- 2D and 3D may differ in rendering treatment, but may not alter the locked silhouette, marking anatomy, orientation, palette data, belly-patch proportion, or whisker attachment logic.

## 8. Allowed scene changes

Pose, expression, action, costume, prop, background, crop, camera, lighting, and atmosphere may change. If clothing or a prop hides a locked marking, do not move the marking to make it visible.

## 9. Common generation failures — mandatory validation

Before delivery, compare against the closest official view and reject/regenerate a result with any of the following:

1. **Triangular profile:** lower face crushed, narrowed, or pointed when rotated.
2. **Wrong head silhouette:** circular sphere, vertically stretched oval, or narrow face instead of an almost-round, slightly horizontally wide oval.
3. **Lost ear wave:** the front-view screen-right brown wave marking is absent, simplified, disconnected, distorted, or mirrored.
4. **Wrong belly patch:** a circle, horizontal oval, off-centre patch, or non-surface-following patch instead of a centred slight vertical oval.
5. **Embedded whiskers:** whiskers look painted/pressed into the face rather than naturally extending from the cheeks in space.
6. **Palette drift/data loss:** any known HEX code is removed, renamed without the code, changed, or incorrectly applied to an unverified pink element.
7. **Unverified specificity:** a count, ratio, contour, colour, or anatomical detail is stated or generated as certain despite not being visible in the relevant approved reference.
8. **Wrong body or limbs:** slim body, long waist, or arms and legs longer than the turnaround; raised arms pressed against the face; an arm stretched to reach a prop instead of the body leaning or rising on tiptoe.
9. **Wrong markings:** arm marking on the outer arm, forearm, armpit or wrong arm, wrong shape (heart, dot, solid oval), or relocated to keep it visible; any extra brown spot on the body.
10. **Missing or miscounted pads:** a palm or sole faces the viewer without its pink pads, shows four toe pads instead of three, or has lost its three toe lobes.
11. **Hidden belly patch:** clothing or a prop covers the whole belly patch without the user accepting it.
12. **Deformed tail:** fails any of the four checks in section 3-1 — squat instead of upright, bumps on the inner edge, a row of equal beads, a smooth paddle, a tapered or detached tail. Verify at magnification; this one is not reliably caught at full-frame size.
13. **Teeth:** any tooth, fang or tooth row, in a still or in any video frame.

## 10. Generation workflow

0. Read `prompts/` first. The approved compact prompt format and the record of what has already failed live there, not in this file.
1. Identify the requested style and camera angle.
2. Open this lock, the relevant style guide, and the nearest turnaround/detail reference.
3. Separate fixed identity from requested scene changes.
4. Generate without mirroring or redesigning locked features.
5. Run the validation checklist above, paying special attention to profile shape, the screen-right ear wave in front view, belly-oval orientation, whisker depth, literal HEX preservation, and the section 3-1 tail comparison at magnification.
6. If a required detail is unverified, defer to the official reference or flag it; do not fill the gap with a guess.
7. Build a scene in stages instead of one prompt: costume & prop first on a plain background, then scene & action, then cutout & layout. See `templates/mongsil-scene.md` section 7.
8. Do not keep re-editing the same generated image. Each extra edit degrades quality and drifts the shape. Allow at most one edit of a result; after that, generate fresh from the approved references. Fix small edges and seams in the design tool instead of regenerating.
9. A petf prop needs its Element **and** its reference sheet attached as a media input. The Element alone gets reinterpreted into a generic object.
10. State plainly when a result could not be verified — in particular, video frames cannot be checked without `ffmpeg`, so the gait, pads, teeth and tail in a clip stay unverified until the user looks at them.
