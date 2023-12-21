Das Projekt zielt darauf ab, älteren Menschen einen barrierefreien Zugang zum Internet zu ermöglichen. Denn: Um einen Computer zu bedienen wird gewissen technisches Vorwissen vorausgesetzt. 
Ich integrierte also ChatGPT-4 in den Pepper, was eine einfache Interaktion durch natürliche Sprache mit einem humanioden Roboter ermöglichte .

Startet man die Anwendung, wird öffnet sich eine HTML Website mit einem großen Button auf dem integrierten Tablet: “Frage stellen”. Klickt man auf diesen startet eine Aufnahme. Das heißt, man kann seine Frage laut aussprechen. Klickt man wieder auf das Tablet wird die Frage abgeschickt und Pepper antwortet unmittelbar.

Im Hintergrund wird die Aufnahme innerhalb des Pepper environments transkribiert und per POST-Request an einen FastAPI-Server gesendet. Dieser leitet die Frage als String an ChatGPT-4 weiter, speichert sie im "Fragenverlauf" und gibt die GPT Antwort zurück.

Das System wurde erfolgreich mit älteren Menschen getestet, wobei besonders die einfache Bedienbarkeit und die Möglichkeit, Fragen in natürlicher Sprache zu stellen, positiv aufgenommen wurden.

----

Dieses Repository beinhaltet nur den Code des lokalen FastAPI Servers.
