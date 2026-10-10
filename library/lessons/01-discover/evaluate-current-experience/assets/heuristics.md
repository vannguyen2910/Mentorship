# Heuristics for AI evaluation (level 1)

Give this file to your AI tool together with your screenshots. It holds the principles, the rules the AI must follow, the output format and two worked examples. Keep it in your AI foundation folder and reuse it on every project.

Source: Nielsen's 10 usability heuristics (NN/g), restated in plain words for this course.

## Rules for the AI

1. Review one family at a time, in the order below. Within a family, check every principle against every screenshot.
2. For each possible problem, give: the step, the exact element or the exact quoted text, and the principle number.
3. Only report what you can point to on a screenshot. If you cannot tell from a still image, write "not sure". Do not guess.
4. Problems that need interaction (undo, back behaviour, loading time, shortcuts) cannot be confirmed from a still image. List them under "Needs interaction to confirm", not as findings.
5. Do not rate severity. Do not suggest redesigns or fixes.
6. Do not repeat the same problem under several principles. Pick the closest one and mention the second in one line.

## Output format

One block per possible problem:

```
- Step: [screen name or number]
- Element: [what you point to, or the exact quoted text]
- Principle: [number and name]
- What I see: [one sentence, observable, no opinion]
- Confidence: sure | not sure
```

End with a list called "Needs interaction to confirm".

## Family 1: Can I see and understand what's going on?

**1. Visibility of system status.** The product tells me what is happening, within a reasonable time.
Check for: loading indicators, confirmation after an action, progress or location markers, live validation.

**2. Match with the real world.** The product speaks my language, not internal jargon, and orders things the way I expect.
Check for: labels users would say themselves, logical order of fields and content, familiar icons.

**6. Recognition over recall.** I should not have to remember things from one screen to the next.
Check for: visible labels, summaries that repeat earlier choices, no values I must remember.

**8. Aesthetic and minimalist design.** Only what matters to the current task is on screen.
Check for: clutter, competing calls to action, content that does not serve the task.

## Family 2: Can I stay in control and recover?

**3. User control and freedom.** I can undo, cancel or go back without penalty.
Check for: undo, cancel, a way out of every step. (Behaviour: needs interaction to confirm.)

**5. Error prevention.** The product stops me from making the mistake in the first place.
Check for: limits on invalid input, confirmation before destructive actions, buttons disabled until ready.

**9. Recognise, diagnose, recover from errors.** Error messages use plain language, say what went wrong and what to do next.
Check for: no error codes alone, a specific cause, a clear next step.

## Family 3: Is it predictable and efficient?

**4. Consistency and standards.** The same thing looks the same and is called the same, inside the product and against common conventions.
Check for: one word per action, one pattern per task, platform norms.

**7. Flexibility and efficiency.** Repeat users can go faster without confusing new users.
Check for: shortcuts, saved defaults, bulk actions, reorder or repeat actions. (Often needs interaction to confirm.)

**10. Help and documentation.** Help is there at the moment I need it, short and about the task.
Check for: explanations next to unfamiliar terms, searchable task-based help.

## Worked examples (different product, for format only)

Example 1, a ride-hailing app, screen "Confirm pickup":
```
- Step: Confirm pickup
- Element: the text "ETA calc pending"
- Principle: 2 Match with the real world
- What I see: the arrival time is labelled "ETA calc pending", a system phrase, instead of plain words such as "Finding your driver"
- Confidence: sure
```

Example 2, the same app, screen "Trip ended":
```
- Step: Trip ended
- Element: the rating stars at the top and a thumbs up/down row at the bottom
- Principle: 4 Consistency and standards
- What I see: two different rating controls appear on one screen for the same purpose
- Confidence: sure
```

Needs interaction to confirm: whether the Back button on "Confirm pickup" cancels the ride request (principle 3).

## After the AI answers

For each item, you ask three questions before it goes into your worksheet:

1. Can I see it on the screen? Point to the exact element.
2. Does it really break that principle?
3. Would a real user hit it?

Yes to all three: add it with a screenshot and rate it yourself. Otherwise discard it. The AI does not rate severity. You do.
