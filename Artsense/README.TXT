# Artsense

> **Status:** Work in progress — actively under development.

A small, research-friendly web app for gathering **one-word reactions** to artworks. Built with Django, Artsense helps you collect quick, minimally-primed emotional or associative responses from viewers, aggregate those responses per artwork, and (optionally) explore patterns across demographic groups such as age or gender.

---

## Purpose

Artsense is designed as a lightweight platform for exploring how people *word* their emotional and associative reactions to visual art. The app intentionally keeps the input minimal — a single word per viewer per artwork — to reduce friction and encourage honest, instinctive responses. The collected data is useful for informal research, classroom projects, and early-stage studies in psychology, sociology, art history, and related fields.

---

## Key ideas & design principles

* **Single-word input:** Users type one word that best describes their immediate reaction. This keeps responses quick and reduces overthinking.
* **Low bias:** Aggregate statistics are hidden by default until after a user submits their response. This reduces conformity and social proof effects.
* **Simple normalization:** Words are normalized (lowercased, trimmed) so basic grouping is possible from the start.
* **Privacy-aware demographics:** Optional demographic breakdowns (e.g., gender, age groups) can be shown, but only when group sizes are large enough to avoid deanonymization.
* **Research-friendly exports:** Data can be exported for further analysis (CSV/JSON) by researchers or educators.

---

## How it works (user flow)

1. The user reads a short explanation about the study and how to respond.
2. The user browses artworks and opens a single-artwork view.
3. The user types a single word describing their reaction and submits it.
4. The app stores the normalized word with minimal metadata (timestamp, artwork id, optional demographic fields).
5. The user can optionally click a button to view aggregated stats for that artwork (top words, counts, percentages, and optional demographic splits).

---

## High-level data model

* **Artwork** — title, image/source id, metadata (e.g., Met Museum id if used).
* **Response** — user (optional), artwork, raw word, normalized word, timestamp.
* **UserProfile** — optional demographic fields (gender, age group) if you collect them.

(Implementation details intentionally omitted here — keep the model minimal while you prototype.)

---

## Privacy & ethics

* **Minimum-group threshold:** Don’t display demographic breakdowns when group counts are low (e.g., fewer than 5–10 responses) to protect anonymity.
* **No public PII:** Avoid exposing personal identifiers in exports or public views.
* **Opt-out & consent:** Make clear to participants how their words will be used and provide an opt-out mechanism.
* **Moderation:** Provide a way to flag or remove abusive/inappropriate words.

---

## Future directions

* Merge synonyms and cluster semantically-similar words (simple dictionary → embeddings).
* Time-based trends and visualization dashboards.
* More refined demographic filters and cross-tabulation (age × gender × location), respecting privacy thresholds.
* Export and API endpoints for academic analysis.

---

## Quick start (prototype)

1. Clone the repo.
2. Create a venv and install requirements.
3. Configure `DJANGO_SECRET_KEY` and DB settings.
4. `python manage.py migrate` and `python manage.py runserver`.
5. Visit the artwork page, submit test responses, and check the simple stats page.

---

## Who might find this useful

* Psychology students studying perception or emotion
* Sociology students exploring cultural or demographic differences
* Art historians or curators interested in public reception
* Educators who want a lightweight class activity or assignment

---

## Contributing

PRs welcome. Please open issues for feature requests and be explicit about privacy implications for new data collection ideas.

---

## License

MIT

---

> Notes: Keep the prototype minimal. Focus on reliable data collection, clear consent language, and conservative privacy safeguards before adding complex analytics.
