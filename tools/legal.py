"""Testi legali del sito OYWA: privacy, cookie, termini e condizioni.

Segnaposto sostituiti da build.py: {MAIL} (link email), {PRIVACY}, {COOKIE},
{TERMS} (URL delle pagine nella stessa lingua). La versione italiana è
l'originale; le altre sono traduzioni.
"""

UPDATED = {
    "it": "Ultimo aggiornamento: 11 ottobre 2026",
    "en": "Last updated: 11 October 2026",
    "es": "Última actualización: 11 de octubre de 2026",
    "pt": "Última atualização: 11 de outubro de 2026",
}

TOC = {"it": "Indice", "en": "Contents", "es": "Índice", "pt": "Índice"}

TRANSLATION_NOTE = {
    "it": "",
    "en": "This is a translation of the Italian original. In case of discrepancies, the Italian version prevails.",
    "es": "Esta es una traducción del original italiano. En caso de discrepancia, prevalece la versión italiana.",
    "pt": "Esta é uma tradução do original em italiano. Em caso de divergência, prevalece a versão em italiano.",
}

# --------------------------------------------------------------------------
# PRIVACY
# --------------------------------------------------------------------------
PRIVACY = {
    "it": {
        "title": "Informativa sulla privacy – OYWA",
        "desc": "Informativa sulla privacy dell'app OYWA e del sito www.oywa.it: i dati dell'app restano sul tuo dispositivo, il sito non usa cookie e conta le visite in forma anonima.",
        "h1": "Informativa sulla privacy",
        "intro": "Questa informativa spiega quali dati trattano l'app OYWA e il sito www.oywa.it, e come.",
        "summary": [
            ("attrazione", "phone", "I dati restano sul telefono", "Nessun server di OYWA, nessun account, nessun login."),
            ("aereo", "globe", "OpenStreetMap per mappa e ricerca", "Solo quando usi la funzione corrispondente."),
            ("ristorante", "ban", "Niente cookie né pubblicità", "Sul sito solo un conteggio anonimo delle visite."),
        ],
        "sections": [
            ("titolare", "Titolare e contatti",
             "<p>Titolare del trattamento: Giuliano Razzicchia. Per qualsiasi domanda sulla privacy: {MAIL}.</p>"
             "<p>Questa informativa riguarda l'app OYWA, un'app per archiviare i luoghi visitati nei viaggi, e il sito www.oywa.it.</p>"),
            ("principio", "Principio di base: i dati dell'app restano sul tuo dispositivo",
             "<p>I dati che inserisci nell'app (luoghi, visite, viaggi, città, persone, voti, note e tutto ciò che salvi) sono conservati esclusivamente nel database locale del tuo telefono. OYWA non ha server propri che ricevono o conservano i tuoi dati, non richiede un account e non richiede il login.</p>"),
            ("terze-parti", "Dati inviati dall'app a servizi di terze parti",
             "<p>Per alcune funzioni l'app contatta servizi esterni. Questi invii avvengono solo quando usi la funzione corrispondente:</p><ul>"
             "<li><strong>Mappa (OpenStreetMap).</strong> Le immagini della mappa sono scaricate dai server di OpenStreetMap (tile.openstreetmap.org). Il server riceve l'indirizzo IP del dispositivo e l'area della mappa che stai guardando.</li>"
             "<li><strong>Ricerca e geocodifica (Nominatim, OpenStreetMap).</strong> Quando cerchi un luogo, il testo della ricerca viene inviato a nominatim.openstreetmap.org. Quando l'app ricava città e paese da una posizione (per esempio durante l'inserimento di un luogo o l'import di un file), le coordinate vengono inviate allo stesso servizio.</li>"
             "<li><strong>App di navigazione.</strong> Quando scegli di aprire un luogo in Mappe, Google Maps o Waze, l'app passa le coordinate a quell'app. Da quel momento si applica la sua informativa.</li></ul>"
             "<p>OYWA non usa strumenti di analisi, pubblicità, crash reporting o tracciamento di terze parti.</p>"),
            ("posizione", "Posizione",
             "<p>L'app può chiedere l'accesso alla posizione del dispositivo, solo mentre la usi, per compilare automaticamente città e paese quando aggiungi un nuovo luogo. La posizione non viene salvata né inviata a OYWA. Le coordinate vengono usate per la richiesta di geocodifica descritta al punto 3. Puoi negare il permesso in qualsiasi momento dalle impostazioni del telefono; le altre funzioni restano disponibili.</p>"),
            ("permessi", "Permessi richiesti dall'app",
             "<ul><li><strong>Posizione (in uso):</strong> facoltativa, descritta al punto 4.</li>"
             "<li><strong>Rete (Internet):</strong> necessaria per la mappa, la ricerca dei luoghi e la geocodifica descritte al punto 3.</li>"
             "<li><strong>File:</strong> l'app legge solo i file che scegli tu, per esempio un backup o un file KML/KMZ da importare, e scrive il file di esportazione che poi condividi.</li></ul>"),
            ("backup", "Backup ed esportazione",
             "<p>Puoi creare un backup completo (file <code>.oywa</code>) o esportare una selezione di luoghi in KML, Excel o PDF. Il file viene creato sul dispositivo e condiviso solo da te, tramite il foglio di condivisione di sistema (per esempio iCloud Drive, Google Drive, mail o messaggi). OYWA non riceve né conserva questi file. Chi riceve un file esportato lo gestisce secondo le proprie regole.</p>"),
            ("perdita", "Perdita del dispositivo o disinstallazione",
             "<p>Poiché i dati sono sul dispositivo, OYWA non può recuperarli. Disinstallando l'app senza un backup, i dati vengono persi. Ti consigliamo di esportare un backup periodicamente e di conservarlo in un luogo sicuro.</p>"),
            ("conservazione", "Conservazione e cancellazione",
             "<p>I dati restano sul dispositivo finché non li elimini tu o disinstalli l'app. Eliminando un luogo o un viaggio, il dato viene rimosso dal database locale.</p>"
             "<p>Puoi cancellare in qualsiasi momento tutto l'archivio (luoghi, visite, viaggi, città e persone) da <strong>Impostazioni → I tuoi dati → Elimina tutti i dati</strong>. La cancellazione è definitiva: se vuoi conservare i dati, esporta prima un backup. Le preferenze dell'app, come la lingua, restano sul dispositivo finché non disinstalli l'app.</p>"),
            ("sito", "Il sito www.oywa.it",
             "<p><strong>Hosting.</strong> Il sito è ospitato da GitHub Pages, un servizio di GitHub, Inc. (Stati Uniti). Quando visiti il sito, i server di GitHub registrano l'indirizzo IP e alcuni dati tecnici della richiesta (browser, pagina richiesta, data e ora) per fornire il servizio e per motivi di sicurezza. Il titolare non ha accesso a questi registri e non li usa. GitHub aderisce all'EU-U.S. Data Privacy Framework; maggiori informazioni sono nell'informativa sulla privacy di GitHub.</p>"
             "<p><strong>Statistiche delle visite (GoatCounter).</strong> Per sapere quante persone visitano il sito usiamo GoatCounter (goatcounter.com), un servizio di statistiche che non usa cookie e non salva nulla sul tuo dispositivo. Quando apri una pagina, il servizio riceve la pagina visitata, il sito da cui arrivi, il tipo di browser e di sistema operativo, le dimensioni dello schermo e il paese, ricavato dall'indirizzo IP. L'indirizzo IP non viene conservato: per distinguere le visite il servizio usa un codice anonimo che cambia ogni giorno, e noi vediamo solo dati aggregati (per esempio «120 visite da Italia, 40 da Spagna»). Non è possibile risalire a chi ha visitato il sito e i dati non vengono usati per pubblicità o profilazione.</p>"
             "<p>La base giuridica è il nostro legittimo interesse a capire quante persone visitano il sito e quali pagine leggono (art. 6, par. 1, lett. f, GDPR). Puoi bloccare il conteggio con un blocco contenuti del browser; il sito funziona comunque.</p>"
             "<p>Il sito non usa cookie né pubblicità. I caratteri tipografici sono ospitati sul sito stesso. I dettagli sono nella <a href=\"{COOKIE}\">cookie policy</a>.</p>"),
            ("email", "Email e richieste per la versione di test",
             "<p>Se ci scrivi a {MAIL}, per esempio per partecipare alla versione di test, trattiamo il tuo indirizzo email, il nome se lo indichi e il contenuto del messaggio. Li usiamo solo per risponderti e, se lo chiedi, per avvisarti quando la versione di test è disponibile e inviarti le istruzioni per installarla.</p>"
             "<p>La base giuridica è la tua richiesta (art. 6, par. 1, lett. b, GDPR) e, per gli avvisi sulla versione di test, il tuo consenso (lett. a), che puoi revocare in ogni momento. La posta elettronica è gestita dal fornitore Register S.p.A. (Italia) e inoltrata a una casella Gmail. Le richieste di partecipazione al test sono registrate in un elenco su Google Drive (indirizzo email, nome se lo indichi, data della richiesta, sistema operativo e lingua) e ricevono una risposta automatica di conferma. Gmail e Google Drive sono servizi di Google (per gli utenti dell'Unione europea, Google Ireland Limited). Conserviamo questi dati per il tempo necessario a gestire la richiesta e, per chi partecipa ai test, fino alla fine della fase di test. Non li cediamo a terzi e non li usiamo per marketing.</p>"),
            ("minori", "Minori",
             "<p>OYWA è destinata a persone che hanno almeno 16 anni. L'app non chiede l'età e non raccoglie dati sui suoi utenti: quello che inserisci resta sul tuo dispositivo e OYWA non lo riceve.</p>"),
            ("diritti", "I tuoi diritti",
             "<p>Ai sensi del Regolamento (UE) 2016/679 (GDPR) hai diritto di accesso, rettifica, cancellazione, limitazione, portabilità e opposizione. Poiché i dati dell'app si trovano sul tuo dispositivo, puoi esercitare la maggior parte di questi diritti direttamente nell'app, anche tramite esportazione o con «Elimina tutti i dati». Per i dati delle email scrivi a {MAIL}. Per le richieste che riguardano i dati trattati dai servizi di terze parti indicati ai punti 3 e 9, rivolgiti direttamente a quei servizi. Hai inoltre diritto di proporre reclamo al Garante per la protezione dei dati personali (garanteprivacy.it).</p>"),
            ("modifiche", "Modifiche",
             "<p>Se questa informativa cambia, aggiorneremo la data in alto e, nei casi rilevanti, te ne daremo notizia nell'app.</p>"),
        ],
    },
    "en": {
        "title": "Privacy policy – OYWA",
        "desc": "Privacy policy of the OYWA app and of www.oywa.it: the app's data stays on your device, and the website uses no cookies and only counts visits anonymously.",
        "h1": "Privacy policy",
        "intro": "This policy explains what data the OYWA app and the www.oywa.it website process, and how.",
        "summary": [
            ("attrazione", "phone", "Your data stays on your phone", "No OYWA servers, no account, no login."),
            ("aereo", "globe", "OpenStreetMap for maps and search", "Only when you use that feature."),
            ("ristorante", "ban", "No cookies or ads", "The website only counts visits anonymously."),
        ],
        "sections": [
            ("titolare", "Controller and contact",
             "<p>Data controller: Giuliano Razzicchia. For any privacy question: {MAIL}.</p>"
             "<p>This policy covers the OYWA app, an app to archive the places you visit when travelling, and the www.oywa.it website.</p>"),
            ("principio", "Basic principle: the app's data stays on your device",
             "<p>The data you enter in the app (places, visits, trips, cities, people, ratings, notes and everything you save) is stored only in the local database on your phone. OYWA has no servers of its own that receive or store your data, and requires neither an account nor a login.</p>"),
            ("terze-parti", "Data the app sends to third-party services",
             "<p>For some features the app contacts external services. This only happens when you use the corresponding feature:</p><ul>"
             "<li><strong>Map (OpenStreetMap).</strong> Map images are downloaded from OpenStreetMap's servers (tile.openstreetmap.org). The server receives your device's IP address and the area of the map you are viewing.</li>"
             "<li><strong>Search and geocoding (Nominatim, OpenStreetMap).</strong> When you search for a place, the search text is sent to nominatim.openstreetmap.org. When the app works out the city and country from a location (for example when adding a place or importing a file), the coordinates are sent to the same service.</li>"
             "<li><strong>Navigation apps.</strong> When you choose to open a place in Apple Maps, Google Maps or Waze, the app passes the coordinates to that app. From then on, that app's privacy policy applies.</li></ul>"
             "<p>OYWA uses no third-party analytics, advertising, crash reporting or tracking tools.</p>"),
            ("posizione", "Location",
             "<p>The app may ask for access to your device's location, only while you use it, to fill in the city and country automatically when you add a new place. The location is neither stored nor sent to OYWA. The coordinates are used for the geocoding request described in section 3. You can deny the permission at any time in your phone's settings; all other features remain available.</p>"),
            ("permessi", "Permissions requested by the app",
             "<ul><li><strong>Location (while in use):</strong> optional, described in section 4.</li>"
             "<li><strong>Network (Internet):</strong> needed for the map, place search and geocoding described in section 3.</li>"
             "<li><strong>Files:</strong> the app only reads files you choose, for example a backup or a KML/KMZ file to import, and writes the export file that you then share.</li></ul>"),
            ("backup", "Backup and export",
             "<p>You can create a full backup (<code>.oywa</code> file) or export a selection of places to KML, Excel or PDF. The file is created on your device and shared only by you, through the system share sheet (for example iCloud Drive, Google Drive, email or messages). OYWA neither receives nor stores these files. Whoever receives an exported file handles it under their own rules.</p>"),
            ("perdita", "Loss of the device or uninstalling",
             "<p>Because the data is on your device, OYWA cannot recover it. If you uninstall the app without a backup, the data is lost. We recommend exporting a backup regularly and keeping it somewhere safe.</p>"),
            ("conservazione", "Retention and deletion",
             "<p>The data stays on your device until you delete it or uninstall the app. When you delete a place or a trip, it is removed from the local database.</p>"
             "<p>You can delete your whole archive (places, visits, trips, cities and people) at any time from <strong>Settings → Your data → Delete all data</strong>. Deletion is permanent: if you want to keep your data, export a backup first. App preferences, such as the language, remain on the device until you uninstall the app.</p>"),
            ("sito", "The www.oywa.it website",
             "<p><strong>Hosting.</strong> The website is hosted on GitHub Pages, a service of GitHub, Inc. (United States). When you visit the site, GitHub's servers log your IP address and some technical data about the request (browser, page requested, date and time) to provide the service and for security purposes. The controller has no access to these logs and does not use them. GitHub participates in the EU-U.S. Data Privacy Framework; more information is in GitHub's privacy statement.</p>"
             "<p><strong>Visit statistics (GoatCounter).</strong> To know how many people visit the site we use GoatCounter (goatcounter.com), an analytics service that uses no cookies and stores nothing on your device. When you open a page, the service receives the page visited, the site you came from, the type of browser and operating system, the screen size and the country, derived from your IP address. The IP address is not stored: to tell visits apart the service uses an anonymous code that changes every day, and we only see aggregated data (for example “120 visits from Italy, 40 from Spain”). It is not possible to identify who visited the site, and the data is not used for advertising or profiling.</p>"
             "<p>The legal basis is our legitimate interest in knowing how many people visit the site and which pages they read (Art. 6(1)(f) GDPR). You can block the count with a content blocker in your browser; the site works anyway.</p>"
             "<p>The website uses no cookies or advertising. The fonts are hosted on the site itself. Details are in the <a href=\"{COOKIE}\">cookie policy</a>.</p>"),
            ("email", "Email and requests for the test version",
             "<p>If you write to us at {MAIL}, for example to join the test version, we process your email address, your name if you give it and the content of your message. We use them only to reply to you and, if you ask, to let you know when the test version is available and send you the instructions to install it.</p>"
             "<p>The legal basis is your request (Art. 6(1)(b) GDPR) and, for notifications about the test version, your consent (Art. 6(1)(a)), which you can withdraw at any time. Email is handled by the provider Register S.p.A. (Italy) and forwarded to a Gmail mailbox. Requests to join the test are recorded in a list on Google Drive (email address, name if you give it, date of the request, operating system and language) and receive an automatic confirmation reply. Gmail and Google Drive are Google services (for users in the European Union, Google Ireland Limited). We keep this data for as long as needed to handle your request and, for testers, until the end of the test phase. We do not share it with third parties and do not use it for marketing.</p>"),
            ("minori", "Minors",
             "<p>OYWA is intended for people aged 16 or over. The app does not ask for your age and collects no data about its users: what you enter stays on your device and OYWA does not receive it.</p>"),
            ("diritti", "Your rights",
             "<p>Under Regulation (EU) 2016/679 (GDPR) you have the right of access, rectification, erasure, restriction, portability and objection. Because the app's data is on your device, you can exercise most of these rights directly in the app, including by exporting or with “Delete all data”. For email data, write to {MAIL}. For requests concerning data processed by the third-party services listed in sections 3 and 9, contact those services directly. You also have the right to lodge a complaint with the Italian Data Protection Authority (garanteprivacy.it) or the supervisory authority of your country.</p>"),
            ("modifiche", "Changes",
             "<p>If this policy changes, we will update the date at the top and, where relevant, let you know in the app.</p>"),
        ],
    },
    "es": {
        "title": "Política de privacidad – OYWA",
        "desc": "Política de privacidad de la app OYWA y de www.oywa.it: los datos de la app se quedan en tu dispositivo y el sitio web no usa cookies y cuenta las visitas de forma anónima.",
        "h1": "Política de privacidad",
        "intro": "Esta política explica qué datos tratan la app OYWA y el sitio web www.oywa.it, y cómo.",
        "summary": [
            ("attrazione", "phone", "Los datos se quedan en el teléfono", "Sin servidores de OYWA, sin cuenta, sin inicio de sesión."),
            ("aereo", "globe", "OpenStreetMap para mapa y búsqueda", "Solo cuando usas esa función."),
            ("ristorante", "ban", "Sin cookies ni publicidad", "El sitio web solo cuenta las visitas de forma anónima."),
        ],
        "sections": [
            ("titolare", "Responsable y contacto",
             "<p>Responsable del tratamiento: Giuliano Razzicchia. Para cualquier consulta sobre privacidad: {MAIL}.</p>"
             "<p>Esta política se refiere a la app OYWA, una app para archivar los lugares visitados en los viajes, y al sitio web www.oywa.it.</p>"),
            ("principio", "Principio básico: los datos de la app se quedan en tu dispositivo",
             "<p>Los datos que introduces en la app (lugares, visitas, viajes, ciudades, personas, valoraciones, notas y todo lo que guardas) se conservan exclusivamente en la base de datos local de tu teléfono. OYWA no tiene servidores propios que reciban o conserven tus datos, y no requiere cuenta ni inicio de sesión.</p>"),
            ("terze-parti", "Datos que la app envía a servicios de terceros",
             "<p>Para algunas funciones la app contacta con servicios externos. Esto solo ocurre cuando usas la función correspondiente:</p><ul>"
             "<li><strong>Mapa (OpenStreetMap).</strong> Las imágenes del mapa se descargan de los servidores de OpenStreetMap (tile.openstreetmap.org). El servidor recibe la dirección IP del dispositivo y la zona del mapa que estás viendo.</li>"
             "<li><strong>Búsqueda y geocodificación (Nominatim, OpenStreetMap).</strong> Cuando buscas un lugar, el texto de la búsqueda se envía a nominatim.openstreetmap.org. Cuando la app deduce la ciudad y el país a partir de una ubicación (por ejemplo al añadir un lugar o importar un archivo), las coordenadas se envían al mismo servicio.</li>"
             "<li><strong>Apps de navegación.</strong> Cuando eliges abrir un lugar en Mapas, Google Maps o Waze, la app pasa las coordenadas a esa app. A partir de ese momento se aplica su política de privacidad.</li></ul>"
             "<p>OYWA no usa herramientas de analítica, publicidad, informes de errores ni rastreo de terceros.</p>"),
            ("posizione", "Ubicación",
             "<p>La app puede pedir acceso a la ubicación del dispositivo, solo mientras la usas, para rellenar automáticamente la ciudad y el país cuando añades un nuevo lugar. La ubicación no se guarda ni se envía a OYWA. Las coordenadas se usan para la solicitud de geocodificación descrita en el punto 3. Puedes denegar el permiso en cualquier momento en los ajustes del teléfono; las demás funciones siguen disponibles.</p>"),
            ("permessi", "Permisos que solicita la app",
             "<ul><li><strong>Ubicación (durante el uso):</strong> opcional, descrita en el punto 4.</li>"
             "<li><strong>Red (Internet):</strong> necesaria para el mapa, la búsqueda de lugares y la geocodificación descritas en el punto 3.</li>"
             "<li><strong>Archivos:</strong> la app solo lee los archivos que eliges, por ejemplo una copia de seguridad o un archivo KML/KMZ para importar, y escribe el archivo de exportación que luego compartes.</li></ul>"),
            ("backup", "Copia de seguridad y exportación",
             "<p>Puedes crear una copia de seguridad completa (archivo <code>.oywa</code>) o exportar una selección de lugares a KML, Excel o PDF. El archivo se crea en el dispositivo y solo lo compartes tú, mediante la hoja para compartir del sistema (por ejemplo iCloud Drive, Google Drive, correo o mensajes). OYWA no recibe ni conserva estos archivos. Quien recibe un archivo exportado lo gestiona según sus propias normas.</p>"),
            ("perdita", "Pérdida del dispositivo o desinstalación",
             "<p>Como los datos están en el dispositivo, OYWA no puede recuperarlos. Si desinstalas la app sin una copia de seguridad, los datos se pierden. Te recomendamos exportar una copia de seguridad periódicamente y guardarla en un lugar seguro.</p>"),
            ("conservazione", "Conservación y eliminación",
             "<p>Los datos permanecen en el dispositivo hasta que los eliminas o desinstalas la app. Al eliminar un lugar o un viaje, se borra de la base de datos local.</p>"
             "<p>Puedes borrar en cualquier momento todo tu archivo (lugares, visitas, viajes, ciudades y personas) desde <strong>Ajustes → Tus datos → Eliminar todos los datos</strong>. La eliminación es definitiva: si quieres conservar los datos, exporta antes una copia de seguridad. Las preferencias de la app, como el idioma, permanecen en el dispositivo hasta que desinstalas la app.</p>"),
            ("sito", "El sitio web www.oywa.it",
             "<p><strong>Alojamiento.</strong> El sitio está alojado en GitHub Pages, un servicio de GitHub, Inc. (Estados Unidos). Cuando visitas el sitio, los servidores de GitHub registran la dirección IP y algunos datos técnicos de la solicitud (navegador, página solicitada, fecha y hora) para prestar el servicio y por motivos de seguridad. El responsable no tiene acceso a estos registros y no los utiliza. GitHub está adherido al EU-U.S. Data Privacy Framework; encontrarás más información en la declaración de privacidad de GitHub.</p>"
             "<p><strong>Estadísticas de visitas (GoatCounter).</strong> Para saber cuántas personas visitan el sitio usamos GoatCounter (goatcounter.com), un servicio de estadísticas que no usa cookies y no guarda nada en tu dispositivo. Cuando abres una página, el servicio recibe la página visitada, el sitio desde el que llegas, el tipo de navegador y de sistema operativo, el tamaño de la pantalla y el país, deducido de la dirección IP. La dirección IP no se conserva: para distinguir las visitas el servicio usa un código anónimo que cambia cada día, y nosotros solo vemos datos agregados (por ejemplo «120 visitas desde Italia, 40 desde España»). No es posible saber quién ha visitado el sitio y los datos no se usan para publicidad ni para elaborar perfiles.</p>"
             "<p>La base jurídica es nuestro interés legítimo en saber cuántas personas visitan el sitio y qué páginas leen (art. 6, apdo. 1, letra f, RGPD). Puedes bloquear el recuento con un bloqueador de contenidos del navegador; el sitio funciona igualmente.</p>"
             "<p>El sitio no usa cookies ni publicidad. Las fuentes tipográficas están alojadas en el propio sitio. Los detalles están en la <a href=\"{COOKIE}\">política de cookies</a>.</p>"),
            ("email", "Correo electrónico y solicitudes para la versión de prueba",
             "<p>Si nos escribes a {MAIL}, por ejemplo para participar en la versión de prueba, tratamos tu dirección de correo, tu nombre si lo indicas y el contenido del mensaje. Solo los usamos para responderte y, si lo pides, para avisarte cuando la versión de prueba esté disponible y enviarte las instrucciones para instalarla.</p>"
             "<p>La base jurídica es tu solicitud (art. 6, apdo. 1, letra b, RGPD) y, para los avisos sobre la versión de prueba, tu consentimiento (letra a), que puedes retirar en cualquier momento. El correo electrónico lo gestiona el proveedor Register S.p.A. (Italia) y se reenvía a un buzón de Gmail. Las solicitudes para participar en la prueba se registran en una lista en Google Drive (dirección de correo, nombre si lo indicas, fecha de la solicitud, sistema operativo e idioma) y reciben una respuesta automática de confirmación. Gmail y Google Drive son servicios de Google (para los usuarios de la Unión Europea, Google Ireland Limited). Conservamos estos datos el tiempo necesario para gestionar la solicitud y, para quienes participan en las pruebas, hasta el final de la fase de prueba. No los cedemos a terceros ni los usamos para marketing.</p>"),
            ("minori", "Menores",
             "<p>OYWA está destinada a personas de al menos 16 años. La app no pregunta la edad y no recopila datos de sus usuarios: lo que introduces se queda en tu dispositivo y OYWA no lo recibe.</p>"),
            ("diritti", "Tus derechos",
             "<p>De acuerdo con el Reglamento (UE) 2016/679 (RGPD) tienes derecho de acceso, rectificación, supresión, limitación, portabilidad y oposición. Como los datos de la app están en tu dispositivo, puedes ejercer la mayoría de estos derechos directamente en la app, también mediante la exportación o con «Eliminar todos los datos». Para los datos de correo, escribe a {MAIL}. Para las solicitudes relativas a los datos tratados por los servicios de terceros indicados en los puntos 3 y 9, dirígete directamente a esos servicios. También tienes derecho a presentar una reclamación ante la autoridad italiana de protección de datos (garanteprivacy.it) o ante la autoridad de control de tu país.</p>"),
            ("modifiche", "Cambios",
             "<p>Si esta política cambia, actualizaremos la fecha de arriba y, cuando sea relevante, te avisaremos en la app.</p>"),
        ],
    },
    "pt": {
        "title": "Política de privacidade – OYWA",
        "desc": "Política de privacidade do app OYWA e do site www.oywa.it: os dados do app ficam no seu dispositivo e o site não usa cookies e conta as visitas de forma anônima.",
        "h1": "Política de privacidade",
        "intro": "Esta política explica quais dados o app OYWA e o site www.oywa.it tratam, e como.",
        "summary": [
            ("attrazione", "phone", "Os dados ficam no celular", "Sem servidores do OYWA, sem conta, sem login."),
            ("aereo", "globe", "OpenStreetMap para mapa e busca", "Só quando você usa a função correspondente."),
            ("ristorante", "ban", "Sem cookies nem anúncios", "O site só conta as visitas de forma anônima."),
        ],
        "sections": [
            ("titolare", "Controlador e contato",
             "<p>Controlador dos dados: Giuliano Razzicchia. Para qualquer dúvida sobre privacidade: {MAIL}.</p>"
             "<p>Esta política se refere ao app OYWA, um app para arquivar os lugares visitados nas viagens, e ao site www.oywa.it.</p>"),
            ("principio", "Princípio básico: os dados do app ficam no seu dispositivo",
             "<p>Os dados que você insere no app (lugares, visitas, viagens, cidades, pessoas, avaliações, notas e tudo o que você salva) ficam guardados exclusivamente no banco de dados local do seu celular. O OYWA não tem servidores próprios que recebam ou guardem os seus dados, e não exige conta nem login.</p>"),
            ("terze-parti", "Dados que o app envia a serviços de terceiros",
             "<p>Para algumas funções o app se conecta a serviços externos. Isso só acontece quando você usa a função correspondente:</p><ul>"
             "<li><strong>Mapa (OpenStreetMap).</strong> As imagens do mapa são baixadas dos servidores do OpenStreetMap (tile.openstreetmap.org). O servidor recebe o endereço IP do dispositivo e a área do mapa que você está vendo.</li>"
             "<li><strong>Busca e geocodificação (Nominatim, OpenStreetMap).</strong> Quando você busca um lugar, o texto da busca é enviado para nominatim.openstreetmap.org. Quando o app descobre a cidade e o país a partir de uma localização (por exemplo ao adicionar um lugar ou importar um arquivo), as coordenadas são enviadas ao mesmo serviço.</li>"
             "<li><strong>Apps de navegação.</strong> Quando você escolhe abrir um lugar no Mapas, Google Maps ou Waze, o app passa as coordenadas para esse app. A partir daí vale a política de privacidade dele.</li></ul>"
             "<p>O OYWA não usa ferramentas de análise, publicidade, relatórios de falhas ou rastreamento de terceiros.</p>"),
            ("posizione", "Localização",
             "<p>O app pode pedir acesso à localização do dispositivo, só enquanto você o usa, para preencher automaticamente a cidade e o país quando você adiciona um novo lugar. A localização não é salva nem enviada ao OYWA. As coordenadas são usadas para a solicitação de geocodificação descrita no item 3. Você pode negar a permissão a qualquer momento nos ajustes do celular; as outras funções continuam disponíveis.</p>"),
            ("permessi", "Permissões solicitadas pelo app",
             "<ul><li><strong>Localização (durante o uso):</strong> opcional, descrita no item 4.</li>"
             "<li><strong>Rede (Internet):</strong> necessária para o mapa, a busca de lugares e a geocodificação descritas no item 3.</li>"
             "<li><strong>Arquivos:</strong> o app só lê os arquivos que você escolhe, por exemplo um backup ou um arquivo KML/KMZ para importar, e grava o arquivo de exportação que você depois compartilha.</li></ul>"),
            ("backup", "Backup e exportação",
             "<p>Você pode criar um backup completo (arquivo <code>.oywa</code>) ou exportar uma seleção de lugares para KML, Excel ou PDF. O arquivo é criado no dispositivo e compartilhado só por você, pela folha de compartilhamento do sistema (por exemplo iCloud Drive, Google Drive, e-mail ou mensagens). O OYWA não recebe nem guarda esses arquivos. Quem recebe um arquivo exportado o trata segundo as próprias regras.</p>"),
            ("perdita", "Perda do dispositivo ou desinstalação",
             "<p>Como os dados estão no dispositivo, o OYWA não pode recuperá-los. Se você desinstalar o app sem um backup, os dados serão perdidos. Recomendamos exportar um backup periodicamente e guardá-lo num lugar seguro.</p>"),
            ("conservazione", "Conservação e exclusão",
             "<p>Os dados ficam no dispositivo até você apagá-los ou desinstalar o app. Ao apagar um lugar ou uma viagem, o dado é removido do banco de dados local.</p>"
             "<p>Você pode apagar a qualquer momento todo o seu arquivo (lugares, visitas, viagens, cidades e pessoas) em <strong>Definições → Seus dados → Apagar todos os dados</strong>. A exclusão é definitiva: se quiser guardar os dados, exporte antes um backup. As preferências do app, como o idioma, ficam no dispositivo até você desinstalar o app.</p>"),
            ("sito", "O site www.oywa.it",
             "<p><strong>Hospedagem.</strong> O site é hospedado no GitHub Pages, um serviço da GitHub, Inc. (Estados Unidos). Quando você visita o site, os servidores do GitHub registram o endereço IP e alguns dados técnicos da solicitação (navegador, página solicitada, data e hora) para prestar o serviço e por motivos de segurança. O controlador não tem acesso a esses registros e não os utiliza. O GitHub aderiu ao EU-U.S. Data Privacy Framework; mais informações estão na declaração de privacidade do GitHub.</p>"
             "<p><strong>Estatísticas de visitas (GoatCounter).</strong> Para saber quantas pessoas visitam o site usamos o GoatCounter (goatcounter.com), um serviço de estatísticas que não usa cookies e não salva nada no seu dispositivo. Quando você abre uma página, o serviço recebe a página visitada, o site de onde você veio, o tipo de navegador e de sistema operacional, o tamanho da tela e o país, obtido a partir do endereço IP. O endereço IP não é guardado: para distinguir as visitas o serviço usa um código anônimo que muda todos os dias, e nós vemos apenas dados agregados (por exemplo “120 visitas da Itália, 40 da Espanha”). Não é possível saber quem visitou o site, e os dados não são usados para publicidade nem para criar perfis.</p>"
             "<p>A base legal é o nosso legítimo interesse em saber quantas pessoas visitam o site e quais páginas leem (art. 6.º, n.º 1, alínea f, do RGPD). Você pode bloquear a contagem com um bloqueador de conteúdo do navegador; o site funciona do mesmo jeito.</p>"
             "<p>O site não usa cookies nem publicidade. As fontes tipográficas ficam hospedadas no próprio site. Os detalhes estão na <a href=\"{COOKIE}\">política de cookies</a>.</p>"),
            ("email", "E-mail e pedidos para a versão de teste",
             "<p>Se você nos escrever em {MAIL}, por exemplo para participar da versão de teste, tratamos o seu endereço de e-mail, o seu nome se você informar e o conteúdo da mensagem. Usamos esses dados só para responder e, se você pedir, para avisar quando a versão de teste estiver disponível e enviar as instruções de instalação.</p>"
             "<p>A base legal é o seu pedido (art. 6.º, n.º 1, alínea b, do RGPD) e, para os avisos sobre a versão de teste, o seu consentimento (alínea a), que você pode retirar a qualquer momento. O e-mail é gerenciado pelo provedor Register S.p.A. (Itália) e encaminhado para uma caixa do Gmail. Os pedidos para participar do teste são registrados numa lista no Google Drive (endereço de e-mail, nome se você informar, data do pedido, sistema operacional e idioma) e recebem uma resposta automática de confirmação. O Gmail e o Google Drive são serviços do Google (para usuários da União Europeia, Google Ireland Limited). Guardamos esses dados pelo tempo necessário para atender ao pedido e, para quem participa dos testes, até o fim da fase de testes. Não os repassamos a terceiros e não os usamos para marketing.</p>"),
            ("minori", "Menores",
             "<p>O OYWA é destinado a pessoas com pelo menos 16 anos. O app não pergunta a idade e não coleta dados dos usuários: o que você insere fica no seu dispositivo e o OYWA não recebe.</p>"),
            ("diritti", "Seus direitos",
             "<p>Nos termos do Regulamento (UE) 2016/679 (RGPD) você tem direito de acesso, retificação, apagamento, limitação, portabilidade e oposição. Como os dados do app estão no seu dispositivo, você pode exercer a maioria desses direitos diretamente no app, inclusive exportando ou com “Apagar todos os dados”. Para os dados de e-mail, escreva para {MAIL}. Para pedidos relativos aos dados tratados pelos serviços de terceiros indicados nos itens 3 e 9, fale diretamente com esses serviços. Você também tem o direito de apresentar reclamação à autoridade italiana de proteção de dados (garanteprivacy.it) ou à autoridade do seu país.</p>"),
            ("modifiche", "Alterações",
             "<p>Se esta política mudar, atualizaremos a data no topo e, quando for relevante, avisaremos você no app.</p>"),
        ],
    },
}

# --------------------------------------------------------------------------
# COOKIE
# --------------------------------------------------------------------------
COOKIE = {
    "it": {
        "title": "Cookie policy – OYWA",
        "desc": "Cookie policy di www.oywa.it: il sito non usa cookie, né tecnici né di terze parti. Unica memorizzazione locale: la lingua scelta, se la scegli tu.",
        "h1": "Cookie policy",
        "intro": "In breve: questo sito non usa cookie. Per questo non trovi nessun banner da accettare.",
        "sections": [
            ("cosa", "Cosa sono i cookie",
             "<p>I cookie sono piccoli file di testo che un sito salva nel browser di chi lo visita. Strumenti simili sono il localStorage e le altre forme di memorizzazione locale del browser. Possono servire a far funzionare il sito (strumenti tecnici) oppure a misurare le visite o a mostrare pubblicità (strumenti analitici e di profilazione).</p>"),
            ("sito", "Cookie usati da www.oywa.it",
             "<p>Nessuno. Il sito www.oywa.it non installa cookie tecnici, analitici, di profilazione o di terze parti. Anche le statistiche delle visite funzionano senza cookie (vedi punto 4).</p>"),
            ("locale", "Memorizzazione locale: la lingua",
             "<p>Se scegli una lingua dal menu in alto, il sito ricorda la scelta salvando nel tuo browser la voce <code>oywa-lang</code> (per esempio «en»). Serve solo a mostrarti il sito nella lingua che hai scelto: non contiene dati personali, non viene inviata a nessun server e resta finché non la cancelli dalle impostazioni del browser. Se non usi il menu, non viene salvato nulla.</p>"
             "<p>È uno strumento tecnico necessario a fornire una funzione che hai richiesto tu, quindi non serve il consenso (art. 122 del Codice in materia di protezione dei dati personali e Linee guida del Garante sui cookie del 10 giugno 2021).</p>"),
            ("terze", "Statistiche delle visite e servizi di terze parti",
             "<p>Per contare le visite il sito usa GoatCounter, un servizio di statistiche che non installa cookie e non salva nulla nel tuo browser: non legge né scrive informazioni sul tuo dispositivo e non ti identifica. Per questo non serve il consenso. Come funziona e quali dati riceve è spiegato nell'<a href=\"{PRIVACY}\">informativa sulla privacy</a>.</p>"
             "<p>Il sito non incorpora altri contenuti di terze parti come mappe, video, pulsanti dei social o caratteri tipografici esterni. Il servizio di hosting, GitHub Pages, non installa cookie.</p>"),
            ("app", "L'app OYWA",
             "<p>Anche l'app OYWA non usa cookie né strumenti di tracciamento. Come tratta i dati è spiegato nell'<a href=\"{PRIVACY}\">informativa sulla privacy</a>.</p>"),
            ("gestire", "Come gestire cookie e memorizzazione locale",
             "<p>Puoi cancellare in ogni momento i dati salvati dai siti, compresa la scelta della lingua, dalle impostazioni del tuo browser (di solito alla voce «Privacy» o «Dati dei siti»).</p>"),
            ("modifiche", "Modifiche e contatti",
             "<p>Se in futuro il sito userà cookie, aggiorneremo questa pagina e, dove necessario, ti chiederemo il consenso prima di installarli. Per domande: {MAIL}.</p>"),
        ],
    },
    "en": {
        "title": "Cookie policy – OYWA",
        "desc": "Cookie policy of www.oywa.it: the website uses no cookies, neither technical nor third-party. The only local storage is your chosen language, if you choose one.",
        "h1": "Cookie policy",
        "intro": "In short: this website uses no cookies. That's why there is no banner to accept.",
        "sections": [
            ("cosa", "What cookies are",
             "<p>Cookies are small text files that a website stores in its visitors' browsers. Similar tools include localStorage and other forms of browser storage. They can be used to make the site work (technical tools) or to measure visits and show ads (analytics and profiling tools).</p>"),
            ("sito", "Cookies used by www.oywa.it",
             "<p>None. The www.oywa.it website sets no technical, analytics, profiling or third-party cookies. Visit statistics also work without cookies (see section 4).</p>"),
            ("locale", "Local storage: language",
             "<p>If you pick a language from the menu at the top, the site remembers your choice by saving the item <code>oywa-lang</code> in your browser (for example “en”). It is only used to show you the site in the language you chose: it contains no personal data, is never sent to any server and stays until you delete it in your browser settings. If you don't use the menu, nothing is saved.</p>"
             "<p>It is a technical tool strictly necessary to provide a feature you asked for, so no consent is required (Art. 122 of the Italian Personal Data Protection Code and the Italian Data Protection Authority's cookie guidelines of 10 June 2021).</p>"),
            ("terze", "Visit statistics and third-party services",
             "<p>To count visits the website uses GoatCounter, an analytics service that sets no cookies and stores nothing in your browser: it neither reads nor writes information on your device and does not identify you. For this reason no consent is required. How it works and what data it receives is explained in the <a href=\"{PRIVACY}\">privacy policy</a>.</p>"
             "<p>The website embeds no other third-party content such as maps, videos, social buttons or external fonts. The hosting service, GitHub Pages, sets no cookies.</p>"),
            ("app", "The OYWA app",
             "<p>The OYWA app also uses no cookies or tracking tools. How it handles data is explained in the <a href=\"{PRIVACY}\">privacy policy</a>.</p>"),
            ("gestire", "Managing cookies and local storage",
             "<p>You can delete the data stored by websites at any time, including your language choice, in your browser settings (usually under “Privacy” or “Site data”).</p>"),
            ("modifiche", "Changes and contact",
             "<p>If the website ever uses cookies, we will update this page and, where required, ask for your consent before setting them. Questions: {MAIL}.</p>"),
        ],
    },
    "es": {
        "title": "Política de cookies – OYWA",
        "desc": "Política de cookies de www.oywa.it: el sitio no usa cookies, ni técnicas ni de terceros. El único almacenamiento local es el idioma elegido, si lo eliges tú.",
        "h1": "Política de cookies",
        "intro": "En resumen: este sitio no usa cookies. Por eso no encontrarás ningún aviso que aceptar.",
        "sections": [
            ("cosa", "Qué son las cookies",
             "<p>Las cookies son pequeños archivos de texto que un sitio web guarda en el navegador de quien lo visita. Herramientas similares son el localStorage y otras formas de almacenamiento local del navegador. Pueden servir para que el sitio funcione (herramientas técnicas) o para medir las visitas y mostrar publicidad (herramientas analíticas y de perfilado).</p>"),
            ("sito", "Cookies que usa www.oywa.it",
             "<p>Ninguna. El sitio www.oywa.it no instala cookies técnicas, analíticas, de perfilado ni de terceros. Las estadísticas de visitas también funcionan sin cookies (ver punto 4).</p>"),
            ("locale", "Almacenamiento local: el idioma",
             "<p>Si eliges un idioma en el menú superior, el sitio recuerda tu elección guardando en tu navegador el elemento <code>oywa-lang</code> (por ejemplo «es»). Solo sirve para mostrarte el sitio en el idioma elegido: no contiene datos personales, no se envía a ningún servidor y permanece hasta que lo borras en los ajustes del navegador. Si no usas el menú, no se guarda nada.</p>"
             "<p>Es una herramienta técnica necesaria para prestar una función que has solicitado, por lo que no requiere consentimiento (art. 122 del Código italiano de protección de datos personales y directrices sobre cookies de la autoridad italiana de protección de datos de 10 de junio de 2021).</p>"),
            ("terze", "Estadísticas de visitas y servicios de terceros",
             "<p>Para contar las visitas el sitio usa GoatCounter, un servicio de estadísticas que no instala cookies y no guarda nada en tu navegador: no lee ni escribe información en tu dispositivo y no te identifica. Por eso no requiere consentimiento. Cómo funciona y qué datos recibe se explica en la <a href=\"{PRIVACY}\">política de privacidad</a>.</p>"
             "<p>El sitio no incorpora otros contenidos de terceros como mapas, vídeos, botones de redes sociales o fuentes externas. El servicio de alojamiento, GitHub Pages, no instala cookies.</p>"),
            ("app", "La app OYWA",
             "<p>La app OYWA tampoco usa cookies ni herramientas de rastreo. Cómo trata los datos se explica en la <a href=\"{PRIVACY}\">política de privacidad</a>.</p>"),
            ("gestire", "Cómo gestionar las cookies y el almacenamiento local",
             "<p>Puedes borrar en cualquier momento los datos guardados por los sitios, incluida la elección del idioma, en los ajustes de tu navegador (normalmente en «Privacidad» o «Datos de sitios»).</p>"),
            ("modifiche", "Cambios y contacto",
             "<p>Si en el futuro el sitio usa cookies, actualizaremos esta página y, cuando sea necesario, te pediremos el consentimiento antes de instalarlas. Consultas: {MAIL}.</p>"),
        ],
    },
    "pt": {
        "title": "Política de cookies – OYWA",
        "desc": "Política de cookies de www.oywa.it: o site não usa cookies, nem técnicos nem de terceiros. O único armazenamento local é o idioma escolhido, se você escolher um.",
        "h1": "Política de cookies",
        "intro": "Resumindo: este site não usa cookies. Por isso não há nenhum aviso para aceitar.",
        "sections": [
            ("cosa", "O que são cookies",
             "<p>Cookies são pequenos arquivos de texto que um site salva no navegador de quem o visita. Ferramentas parecidas são o localStorage e outras formas de armazenamento local do navegador. Podem servir para fazer o site funcionar (ferramentas técnicas) ou para medir visitas e mostrar anúncios (ferramentas analíticas e de perfil).</p>"),
            ("sito", "Cookies usados por www.oywa.it",
             "<p>Nenhum. O site www.oywa.it não instala cookies técnicos, analíticos, de perfil nem de terceiros. As estatísticas de visitas também funcionam sem cookies (ver item 4).</p>"),
            ("locale", "Armazenamento local: o idioma",
             "<p>Se você escolher um idioma no menu do topo, o site lembra a escolha salvando no seu navegador o item <code>oywa-lang</code> (por exemplo “pt”). Ele só serve para mostrar o site no idioma escolhido: não contém dados pessoais, não é enviado a nenhum servidor e fica até você apagá-lo nas configurações do navegador. Se você não usar o menu, nada é salvo.</p>"
             "<p>É uma ferramenta técnica necessária para oferecer uma função que você pediu, por isso não exige consentimento (art. 122 do Código italiano de proteção de dados pessoais e diretrizes sobre cookies da autoridade italiana de proteção de dados de 10 de junho de 2021).</p>"),
            ("terze", "Estatísticas de visitas e serviços de terceiros",
             "<p>Para contar as visitas o site usa o GoatCounter, um serviço de estatísticas que não instala cookies e não salva nada no seu navegador: não lê nem grava informações no seu dispositivo e não identifica você. Por isso não exige consentimento. Como funciona e quais dados recebe está explicado na <a href=\"{PRIVACY}\">política de privacidade</a>.</p>"
             "<p>O site não incorpora outros conteúdos de terceiros como mapas, vídeos, botões de redes sociais ou fontes externas. O serviço de hospedagem, GitHub Pages, não instala cookies.</p>"),
            ("app", "O app OYWA",
             "<p>O app OYWA também não usa cookies nem ferramentas de rastreamento. Como ele trata os dados está explicado na <a href=\"{PRIVACY}\">política de privacidade</a>.</p>"),
            ("gestire", "Como gerenciar cookies e armazenamento local",
             "<p>Você pode apagar a qualquer momento os dados salvos pelos sites, incluindo a escolha do idioma, nas configurações do seu navegador (normalmente em “Privacidade” ou “Dados de sites”).</p>"),
            ("modifiche", "Alterações e contato",
             "<p>Se no futuro o site usar cookies, atualizaremos esta página e, quando necessário, pediremos o seu consentimento antes de instalá-los. Dúvidas: {MAIL}.</p>"),
        ],
    },
}

# --------------------------------------------------------------------------
# TERMINI E CONDIZIONI
# --------------------------------------------------------------------------
TERMS = {
    "it": {
        "title": "Termini e condizioni – OYWA",
        "desc": "Termini e condizioni d'uso dell'app OYWA e del sito www.oywa.it: versione di test gratuita, dati sul tuo dispositivo, età minima 16 anni.",
        "h1": "Termini e condizioni",
        "intro": "Questi termini regolano l'uso dell'app OYWA e del sito www.oywa.it. Usandoli, li accetti.",
        "sections": [
            ("chi", "Chi siamo",
             "<p>OYWA è il progetto che sviluppa l'app OYWA e il sito www.oywa.it (di seguito «noi»). I dati del titolare sono indicati nell'<a href=\"{PRIVACY}\">informativa sulla privacy</a>. Per qualsiasi comunicazione: {MAIL}.</p>"),
            ("requisiti", "Chi può usare OYWA",
             "<p>OYWA è destinata a persone che hanno almeno 16 anni. Usando l'app confermi di avere almeno questa età.</p>"),
            ("servizio", "Il servizio",
             "<p>OYWA è un'app per archiviare i luoghi visitati nei viaggi. La versione di test è gratuita: non contiene acquisti né abbonamenti e non mostra pubblicità. Prezzo e condizioni della versione definitiva saranno comunicati al lancio.</p>"
             "<p>L'app è attualmente in fase di test: può contenere errori e le sue funzioni possono cambiare, essere aggiunte o rimosse. Possiamo sospendere o terminare la versione di test in qualsiasi momento; i dati già salvati restano comunque sul tuo dispositivo.</p>"),
            ("dati", "I tuoi dati e i backup",
             "<p>I contenuti che inserisci restano tuoi e sono salvati solo sul tuo dispositivo, come spiegato nell'<a href=\"{PRIVACY}\">informativa sulla privacy</a>. Non abbiamo accesso ai tuoi dati e non possiamo recuperarli se vengono persi, per esempio se il telefono si rompe o se disinstalli l'app.</p>"
             "<p>Sei responsabile di creare e conservare i backup. L'app offre a questo scopo l'esportazione di un backup completo e, se lo attivi, un promemoria mensile.</p>"),
            ("uso", "Uso consentito",
             "<p>Puoi usare OYWA per scopi personali. Non puoi usarla per attività illecite, per violare i diritti di altri o per sovraccaricare i servizi esterni di cui si serve, per esempio facendo richieste automatiche in massa ai servizi di OpenStreetMap.</p>"),
            ("terze", "Servizi di terze parti",
             "<p>Per mappe, ricerca e geocodifica OYWA usa i servizi di OpenStreetMap; per la navigazione può aprire app esterne come Mappe, Google Maps o Waze. A questi servizi si applicano i rispettivi termini. I dati delle mappe sono © contributori di OpenStreetMap, disponibili con licenza Open Database License (ODbL). Non siamo responsabili della disponibilità o dell'accuratezza dei servizi di terze parti.</p>"),
            ("proprieta", "Proprietà intellettuale",
             "<p>Il nome e il marchio OYWA, la grafica, le illustrazioni, i testi e il software dell'app e del sito appartengono a noi o ai rispettivi titolari. Non puoi copiarli, modificarli o distribuirli senza autorizzazione, salvo quanto consentito dalla legge.</p>"),
            ("garanzie", "Garanzie e responsabilità",
             "<p>OYWA è fornita gratuitamente, «così com'è». Ci impegniamo perché funzioni bene, ma non garantiamo che sia priva di errori o sempre disponibile.</p>"
             "<p>Nei limiti consentiti dalla legge, non siamo responsabili per la perdita di dati salvati sul dispositivo o per danni indiretti derivanti dall'uso dell'app. Restano salve la responsabilità per dolo o colpa grave e i diritti che la legge riconosce in modo inderogabile ai consumatori.</p>"),
            ("modifiche", "Modifiche ai termini",
             "<p>Possiamo aggiornare questi termini, per esempio quando l'app cambia. Pubblicheremo la nuova versione su questa pagina con la data di aggiornamento e, per le modifiche importanti, te ne daremo notizia nell'app.</p>"),
            ("legge", "Legge applicabile",
             "<p>Questi termini sono regolati dalla legge italiana. Se sei un consumatore, restano salve le tutele inderogabili previste dalla legge del paese in cui risiedi, e per eventuali controversie è competente il giudice del luogo della tua residenza o del tuo domicilio.</p>"),
            ("contatti", "Contatti",
             "<p>Per domande, segnalazioni o reclami scrivi a {MAIL}.</p>"),
        ],
    },
    "en": {
        "title": "Terms and conditions – OYWA",
        "desc": "Terms and conditions of use of the OYWA app and the www.oywa.it website: free test version, data on your device, minimum age 16.",
        "h1": "Terms and conditions",
        "intro": "These terms govern the use of the OYWA app and the www.oywa.it website. By using them, you accept these terms.",
        "sections": [
            ("chi", "Who we are",
             "<p>OYWA is the project that develops the OYWA app and the www.oywa.it website (“we”). The controller's details are given in the <a href=\"{PRIVACY}\">privacy policy</a>. For any communication: {MAIL}.</p>"),
            ("requisiti", "Who can use OYWA",
             "<p>OYWA is intended for people aged 16 or over. By using the app you confirm that you are at least that age.</p>"),
            ("servizio", "The service",
             "<p>OYWA is an app to archive the places you visit when travelling. The test version is free: it has no purchases or subscriptions and shows no ads. The price and terms of the final version will be announced at launch.</p>"
             "<p>The app is currently in testing: it may contain errors and its features may change, be added or be removed. We may suspend or end the test version at any time; the data you have already saved stays on your device.</p>"),
            ("dati", "Your data and backups",
             "<p>The content you enter remains yours and is stored only on your device, as explained in the <a href=\"{PRIVACY}\">privacy policy</a>. We have no access to your data and cannot recover it if it is lost, for example if your phone breaks or you uninstall the app.</p>"
             "<p>You are responsible for creating and keeping backups. For this purpose the app lets you export a full backup and, if you turn it on, offers a monthly reminder.</p>"),
            ("uso", "Permitted use",
             "<p>You may use OYWA for personal purposes. You may not use it for unlawful activities, to infringe other people's rights or to overload the external services it relies on, for example by sending mass automated requests to OpenStreetMap services.</p>"),
            ("terze", "Third-party services",
             "<p>For maps, search and geocoding OYWA uses OpenStreetMap services; for navigation it can open external apps such as Apple Maps, Google Maps or Waze. Those services' own terms apply. Map data is © OpenStreetMap contributors, available under the Open Database License (ODbL). We are not responsible for the availability or accuracy of third-party services.</p>"),
            ("proprieta", "Intellectual property",
             "<p>The OYWA name and brand, the design, illustrations, texts and software of the app and website belong to us or to their respective owners. You may not copy, modify or distribute them without permission, except as permitted by law.</p>"),
            ("garanzie", "Warranties and liability",
             "<p>OYWA is provided free of charge, “as is”. We do our best to make it work well, but we do not guarantee that it is error-free or always available.</p>"
             "<p>To the extent permitted by law, we are not liable for the loss of data stored on your device or for indirect damages arising from the use of the app. This does not affect liability for wilful misconduct or gross negligence, nor the rights that the law grants consumers and that cannot be waived.</p>"),
            ("modifiche", "Changes to these terms",
             "<p>We may update these terms, for example when the app changes. We will publish the new version on this page with the update date and, for important changes, let you know in the app.</p>"),
            ("legge", "Governing law",
             "<p>These terms are governed by Italian law. If you are a consumer, you keep the mandatory protections of the law of the country where you live, and any dispute falls under the jurisdiction of the courts of your place of residence or domicile.</p>"),
            ("contatti", "Contact",
             "<p>For questions, reports or complaints write to {MAIL}.</p>"),
        ],
    },
    "es": {
        "title": "Términos y condiciones – OYWA",
        "desc": "Términos y condiciones de uso de la app OYWA y del sitio www.oywa.it: versión de prueba gratuita, datos en tu dispositivo, edad mínima 16 años.",
        "h1": "Términos y condiciones",
        "intro": "Estos términos regulan el uso de la app OYWA y del sitio www.oywa.it. Al usarlos, los aceptas.",
        "sections": [
            ("chi", "Quiénes somos",
             "<p>OYWA es el proyecto que desarrolla la app OYWA y el sitio www.oywa.it («nosotros»). Los datos del responsable figuran en la <a href=\"{PRIVACY}\">política de privacidad</a>. Para cualquier comunicación: {MAIL}.</p>"),
            ("requisiti", "Quién puede usar OYWA",
             "<p>OYWA está destinada a personas de al menos 16 años. Al usar la app confirmas que tienes al menos esa edad.</p>"),
            ("servizio", "El servicio",
             "<p>OYWA es una app para archivar los lugares visitados en los viajes. La versión de prueba es gratuita: no incluye compras ni suscripciones y no muestra publicidad. El precio y las condiciones de la versión definitiva se anunciarán en el lanzamiento.</p>"
             "<p>La app está actualmente en fase de prueba: puede contener errores y sus funciones pueden cambiar, añadirse o eliminarse. Podemos suspender o finalizar la versión de prueba en cualquier momento; los datos ya guardados permanecen en tu dispositivo.</p>"),
            ("dati", "Tus datos y las copias de seguridad",
             "<p>Los contenidos que introduces siguen siendo tuyos y solo se guardan en tu dispositivo, como se explica en la <a href=\"{PRIVACY}\">política de privacidad</a>. No tenemos acceso a tus datos y no podemos recuperarlos si se pierden, por ejemplo si el teléfono se rompe o desinstalas la app.</p>"
             "<p>Eres responsable de crear y conservar las copias de seguridad. Para ello la app permite exportar una copia completa y, si lo activas, ofrece un recordatorio mensual.</p>"),
            ("uso", "Uso permitido",
             "<p>Puedes usar OYWA con fines personales. No puedes usarla para actividades ilícitas, para vulnerar derechos ajenos ni para sobrecargar los servicios externos que utiliza, por ejemplo enviando solicitudes automáticas masivas a los servicios de OpenStreetMap.</p>"),
            ("terze", "Servicios de terceros",
             "<p>Para mapas, búsqueda y geocodificación OYWA usa los servicios de OpenStreetMap; para la navegación puede abrir apps externas como Mapas, Google Maps o Waze. A estos servicios se aplican sus propios términos. Los datos de los mapas son © colaboradores de OpenStreetMap, disponibles con licencia Open Database License (ODbL). No somos responsables de la disponibilidad ni de la exactitud de los servicios de terceros.</p>"),
            ("proprieta", "Propiedad intelectual",
             "<p>El nombre y la marca OYWA, el diseño, las ilustraciones, los textos y el software de la app y del sitio nos pertenecen a nosotros o a sus respectivos titulares. No puedes copiarlos, modificarlos ni distribuirlos sin autorización, salvo en lo permitido por la ley.</p>"),
            ("garanzie", "Garantías y responsabilidad",
             "<p>OYWA se ofrece gratuitamente, «tal cual». Nos esforzamos para que funcione bien, pero no garantizamos que esté libre de errores ni que esté siempre disponible.</p>"
             "<p>En la medida permitida por la ley, no somos responsables de la pérdida de datos guardados en el dispositivo ni de los daños indirectos derivados del uso de la app. Queda a salvo la responsabilidad por dolo o culpa grave y los derechos irrenunciables que la ley reconoce a los consumidores.</p>"),
            ("modifiche", "Cambios en los términos",
             "<p>Podemos actualizar estos términos, por ejemplo cuando cambie la app. Publicaremos la nueva versión en esta página con la fecha de actualización y, para los cambios importantes, te avisaremos en la app.</p>"),
            ("legge", "Ley aplicable",
             "<p>Estos términos se rigen por la ley italiana. Si eres consumidor, conservas las protecciones irrenunciables de la ley del país donde resides, y para cualquier controversia son competentes los tribunales de tu lugar de residencia o domicilio.</p>"),
            ("contatti", "Contacto",
             "<p>Para preguntas, avisos o reclamaciones escribe a {MAIL}.</p>"),
        ],
    },
    "pt": {
        "title": "Termos e condições – OYWA",
        "desc": "Termos e condições de uso do app OYWA e do site www.oywa.it: versão de teste gratuita, dados no seu dispositivo, idade mínima de 16 anos.",
        "h1": "Termos e condições",
        "intro": "Estes termos regulam o uso do app OYWA e do site www.oywa.it. Ao usá-los, você os aceita.",
        "sections": [
            ("chi", "Quem somos",
             "<p>O OYWA é o projeto que desenvolve o app OYWA e o site www.oywa.it (“nós”). Os dados do controlador estão na <a href=\"{PRIVACY}\">política de privacidade</a>. Para qualquer comunicação: {MAIL}.</p>"),
            ("requisiti", "Quem pode usar o OYWA",
             "<p>O OYWA é destinado a pessoas com pelo menos 16 anos. Ao usar o app você confirma ter pelo menos essa idade.</p>"),
            ("servizio", "O serviço",
             "<p>O OYWA é um app para arquivar os lugares visitados nas viagens. A versão de teste é gratuita: não tem compras nem assinaturas e não mostra anúncios. O preço e as condições da versão final serão anunciados no lançamento.</p>"
             "<p>O app está atualmente em fase de testes: pode conter erros e as suas funções podem mudar, ser adicionadas ou removidas. Podemos suspender ou encerrar a versão de teste a qualquer momento; os dados já salvos continuam no seu dispositivo.</p>"),
            ("dati", "Seus dados e os backups",
             "<p>Os conteúdos que você insere continuam sendo seus e ficam salvos só no seu dispositivo, como explicado na <a href=\"{PRIVACY}\">política de privacidade</a>. Não temos acesso aos seus dados e não podemos recuperá-los se forem perdidos, por exemplo se o celular quebrar ou se você desinstalar o app.</p>"
             "<p>Você é responsável por criar e guardar os backups. Para isso o app permite exportar um backup completo e, se você ativar, oferece um lembrete mensal.</p>"),
            ("uso", "Uso permitido",
             "<p>Você pode usar o OYWA para fins pessoais. Não pode usá-lo para atividades ilícitas, para violar direitos de outras pessoas ou para sobrecarregar os serviços externos que ele utiliza, por exemplo enviando solicitações automáticas em massa aos serviços do OpenStreetMap.</p>"),
            ("terze", "Serviços de terceiros",
             "<p>Para mapas, busca e geocodificação o OYWA usa os serviços do OpenStreetMap; para a navegação pode abrir apps externos como Mapas, Google Maps ou Waze. A esses serviços se aplicam os respectivos termos. Os dados dos mapas são © colaboradores do OpenStreetMap, disponíveis sob a licença Open Database License (ODbL). Não somos responsáveis pela disponibilidade ou precisão dos serviços de terceiros.</p>"),
            ("proprieta", "Propriedade intelectual",
             "<p>O nome e a marca OYWA, o design, as ilustrações, os textos e o software do app e do site pertencem a nós ou aos respectivos titulares. Você não pode copiá-los, modificá-los ou distribuí-los sem autorização, exceto no que a lei permitir.</p>"),
            ("garanzie", "Garantias e responsabilidade",
             "<p>O OYWA é oferecido gratuitamente, “no estado em que se encontra”. Fazemos o possível para que funcione bem, mas não garantimos que esteja livre de erros ou sempre disponível.</p>"
             "<p>Nos limites permitidos pela lei, não somos responsáveis pela perda de dados salvos no dispositivo nem por danos indiretos decorrentes do uso do app. Ficam ressalvadas a responsabilidade por dolo ou culpa grave e os direitos que a lei reconhece de forma irrenunciável aos consumidores.</p>"),
            ("modifiche", "Alterações dos termos",
             "<p>Podemos atualizar estes termos, por exemplo quando o app mudar. Publicaremos a nova versão nesta página com a data de atualização e, para mudanças importantes, avisaremos você no app.</p>"),
            ("legge", "Lei aplicável",
             "<p>Estes termos são regidos pela lei italiana. Se você é consumidor, continuam valendo as proteções obrigatórias da lei do país onde reside, e eventuais disputas serão de competência do foro do seu domicílio.</p>"),
            ("contatti", "Contato",
             "<p>Para dúvidas, avisos ou reclamações escreva para {MAIL}.</p>"),
        ],
    },
}
