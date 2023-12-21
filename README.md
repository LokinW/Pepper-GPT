Das Projekt zielt darauf ab, älteren Menschen einen barrierefreien Zugang zum Internet zu ermöglichen, indem ChatGPT-4 in den Pepper Roboter integriert wird.

Startet man die Anwendung, wird öffnet sich eine HTML Website auf dem integrierten Tablet: “Frage stellen”. Bei Betätigung des Buttons sendet die Anwendung einen POST-Request an einen FastAPI-Server, der die Frage an ChatGPT-4 weiterleitet, im "Fragenverlauf" speichert und die erhaltene Antwort zurückgibt. Der Pepper Roboter spricht die Antwort aus, wodurch eine natürliche Interaktion entsteht.

Das System wurde erfolgreich mit älteren Menschen getestet, wobei besonders die einfache Bedienbarkeit und die Möglichkeit, Fragen in natürlicher Sprache zu stellen, positiv aufgenommen wurden.

Dieses Repository beinhaltet nur den Code des lokalen Servers.
