# -*- coding: utf-8 -*-
# Content for Amanda Britto CVs — 3 profiles × 3 languages (en, pt, fr)
# Decision log: no BR phone anywhere; FR versions keep EN job titles;
# games profile merges Narrative Design + LQA.

LABELS = {
  "en": dict(contact="Contact", core="Core Skills", general="General Skills", tech="Technical",
             langs="Languages", certs="Certifications", profile="Profile",
             exp="Professional Experience", cont="Professional Experience — continued",
             edu="Academic Education", qual="Professional Qualification",
             awards="Awards", online="Online", page="Page",
             loc="Location", phone="Phone", mail="E-mail",
             l_enpt="English & Portuguese", l_fr="French", l_es="Spanish"),
  "pt": dict(contact="Contato", core="Competências", general="Competências Gerais", tech="Técnico",
             langs="Idiomas", certs="Certificações", profile="Perfil",
             exp="Experiência Profissional", cont="Experiência Profissional — continuação",
             edu="Formação Acadêmica", qual="Qualificação Profissional",
             awards="Prêmios", online="Online", page="Página",
             loc="Localização", phone="Telefone", mail="E-mail",
             l_enpt="Inglês & Português", l_fr="Francês", l_es="Espanhol"),
  "fr": dict(contact="Contact", core="Compétences clés", general="Compétences générales", tech="Technique",
             langs="Langues", certs="Certifications", profile="Profil",
             exp="Expérience professionnelle", cont="Expérience professionnelle — suite",
             edu="Formation académique", qual="Qualification professionnelle",
             awards="Prix & distinctions", online="En ligne", page="Page",
             loc="Localisation", phone="Téléphone", mail="Courriel",
             l_enpt="Anglais & portugais", l_fr="Français", l_es="Espagnol"),
}

CONTACT = [("LinkedIn", "/in/amandareznor"), ("Credly", "/users/amanda-reznor-britto")]
PHONE = "+1 (418) 446-0091"
MAIL = "ab.murtinho@hotmail.com"
LOCATION = "Montréal — QC, Canada"
LOCATION_L = {"en": "Montréal — QC, Canada", "pt": "Montréal — QC, Canadá", "fr": "Montréal — QC, Canada"}

CERTS = {
  "en": ["Google Data Analytics", "Google Cloud Computing Foundations", "Prompt Engineering",
         "CELPIP English — Level 10", "Programme de francisation du Québec — niv. 8"],
  "pt": ["Google Data Analytics", "Google Cloud Computing Foundations", "Prompt Engineering",
         "CELPIP English — Nível 10", "Programa de Francisação do Québec — nível 8"],
  "fr": ["Google Data Analytics", "Google Cloud Computing Foundations", "Prompt Engineering",
         "CELPIP English — niveau 10", "Programme de francisation du Québec — niv. 8"],
}

# Shared education entries -----------------------------------------------------
def EDU(lang, keys):
    E = {
      "ma_lit": {
        "en": ("Master's Degree in Literature", "University of São Paulo (USP) · 2019 – 2023 · São Paulo, Brazil"),
        "pt": ("Mestrado em Letras", "Universidade de São Paulo (USP) · 2019 – 2023 · São Paulo, Brasil"),
        "fr": ("Master's Degree in Literature (maîtrise ès lettres)", "Université de São Paulo (USP) · 2019 – 2023 · São Paulo, Brésil"),
      },
      "ma_edu": {
        "en": ("Master's Degree in Professional Education", "CEETEPS — Centro Paula Souza · 2016 – 2017 · São Paulo, Brazil · validated by ECA (Educational Credential Assessment)"),
        "pt": ("Mestrado em Educação Profissional", "CEETEPS — Centro Paula Souza · 2016 – 2017 · São Paulo, Brasil · validado por ECA (Educational Credential Assessment)"),
        "fr": ("Master's Degree in Professional Education (maîtrise en éducation)", "CEETEPS — Centro Paula Souza · 2016 – 2017 · São Paulo, Brésil · validée par l'EDE / ECA (Educational Credential Assessment)"),
      },
      "spec_games": {
        "en": ("Specialization in Digital Games", "Metropolitan University Center — FMU · 2015 – 2016 · São Paulo, Brazil"),
        "pt": ("Especialização em Jogos Digitais", "Centro Universitário FMU · 2015 – 2016 · São Paulo, Brasil"),
        "fr": ("Specialization in Digital Games (études supérieures spécialisées)", "Centre universitaire FMU · 2015 – 2016 · São Paulo, Brésil"),
      },
      "bsc_cs": {
        "en": ("Bachelor of Computer Science", "Metropolitan University Center — FMU · 2020 – 2024 · São Paulo, Brazil"),
        "pt": ("Bacharelado em Ciência da Computação", "Centro Universitário FMU · 2020 – 2024 · São Paulo, Brasil"),
        "fr": ("Bachelor of Computer Science (baccalauréat en informatique)", "Centre universitaire FMU · 2020 – 2024 · São Paulo, Brésil"),
      },
      "tech_web": {
        "en": ("Internet Systems Technologist", "Universidade Nove de Julho — UNINOVE · 2011 – 2013 · São Paulo, Brazil"),
        "pt": ("Tecnólogo em Sistemas para Internet", "Universidade Nove de Julho — UNINOVE · 2011 – 2013 · São Paulo, Brasil"),
        "fr": ("Internet Systems Technologist (technologue en systèmes Internet)", "Universidade Nove de Julho — UNINOVE · 2011 – 2013 · São Paulo, Brésil"),
      },
    }
    return [E[k][lang] for k in keys]

DOTS5 = '● ● ● ● ●'
DOTS4 = '● ● ● ● <span class="off">●</span>'
DOTS3 = '● ● ● <span class="off">● ●</span>'

def LANGS(lang):
    L = LABELS[lang]
    return [(L["l_enpt"], DOTS5), (L["l_fr"], DOTS4), (L["l_es"], DOTS3)]

# =============================================================================
# PROFILE A — DATA ANALYST
# =============================================================================
DATA_ANALYST = {
 "en": dict(
  role="Data Analyst",
  tag="Data Quality · Product &amp; Game Analytics · Data Storytelling",
  foot="DATA ANALYST",
  core=["Data quality &amp; evaluation","Exploratory data analysis","A/B testing &amp; comparative analysis",
        "Dashboards (Power BI, Looker)","Data storytelling &amp; visualization","Product &amp; funnel analysis",
        "Cross-functional collaboration"],
  tech=["SQL queries","Python for analytics","HTML, CSS, JavaScript","Jira · Redmine · Google Sheets",
        "Documentation &amp; content production","E-learning platforms"],
  prof="Data Analyst with strong experience across <b>technology, education, and game production</b>, specialized in <b>data quality</b>, <b>user behavior</b>, and <b>product insights</b>. Proven ability to translate complex data into actionable insights through <b>SQL, Python, dashboards</b>, and <b>data storytelling</b> — supported by Google certifications in <b>Data Analytics</b> and <b>Cloud Computing Foundations</b>, two Master's degrees, and hands-on work with live production pipelines, QA workflows, and user-facing systems across mobile, PC, and console platforms.",
  jobs1=[
   dict(t="Data Analyst", at="TELUS Digital", meta="2026 – present · Montréal, Canada", b=[
     "Perform <b>data quality assessment</b> for map-based queries, ensuring <b>accuracy</b> and <b>consistency</b> of geospatial information.",
     "Analyze <b>POI</b> (Points of Interest), <b>SBS</b> (Search, Browse &amp; Services), and <b>audio datasets</b>, evaluating query relevance, identifying discrepancies, and providing structured feedback that improves search quality.",
     "Contribute to the continuous improvement of <b>data quality processes</b>, supporting reliable, decision-ready databases."]),
   dict(t="LQA Test Analyst", at="GlobalStep", meta="2025 – present · Montréal, Canada", b=[
     "Evaluate <b>game content quality</b> with focus on <b>narrative consistency</b>, <b>localization accuracy</b>, usability, and player-facing functionality.",
     "Contribute quality insights for <b>AA/AAA titles</b> — including <b>Football Manager 26</b> and <b>Marvel Contest of Champions</b> — across mobile, PC, and console, supporting <b>data-informed decisions</b> on player experience.",
     "<b>Document findings</b> and track issues through structured workflows (Jira, Redmine, Google Sheets), collaborating with design, production, QA, and clients."]),
   dict(t="Academic Coordinator &amp; IT Professor", at="FMU, FAM, Impacta, UNICAP, UniBTA", meta="2018 – 2025 · São Paulo, Brazil", b=[
     "Led <b>data-driven monitoring</b> of academic performance, engagement, and retention metrics, working with multidisciplinary teams to improve outcomes based on <b>KPIs</b>.",
     "Taught 30+ courses in <b>databases</b>, <b>programming</b>, <b>analytics</b>, game development, and project management.",
     "Produced <b>reports, dashboards, and documentation</b> supporting strategic decision-making."]),
  ],
  jobs2=[
   dict(t="Game &amp; Narrative Designer", at="Multiple Studios", meta="2018 – 2023 · São Paulo, Brazil", b=[
     "Designed <b>player progression systems</b>, <b>engagement loops</b>, and narrative-driven retention mechanics.",
     "Analyzed <b>player interaction patterns</b> to align game mechanics with user behavior, balancing gameplay and monetization with designers, developers, and artists.",
     "Produced <b>GDDs, whitepapers</b>, and documentation supporting <b>data-informed design</b> decisions."]),
   dict(t="Conversational Designer", at="Selected Projects", meta="2019 – 2020 · São Paulo, Brazil", b=[
     "Designed and evaluated <b>conversational flows</b> and <b>decision trees</b> for interactive digital experiences, identifying friction points and improving <b>user engagement</b>."]),
   dict(t="Census Agent", at="IBGE, Brazilian Institute of Geography and Statistics", meta="2010 · São Paulo, Brazil", b=[
     "Collected, validated, and analyzed population data for official statistical reporting, ensuring <b>data accuracy and consistency</b> for large-scale datasets."]),
  ],
  awards=["2<sup>nd</sup> place — Uber Hack, 2019","Winner — Global Game Jam (Mimix VR), 2018",
          "1<sup>st</sup> place — Hackathon Cotidiano VR, 2017","1<sup>st</sup> place — Hack Engage, Campus Party Experience"],
  online=[("Portfolio","amandareznor.netlify.app/britto"),("Lattes","goo.gl/qd2oWR")],
  edu_keys=["ma_edu","ma_lit","spec_games","bsc_cs"],
 ),
 "pt": dict(
  role="Analista de Dados",
  tag="Qualidade de Dados · Análise de Produto &amp; Games · Data Storytelling",
  foot="ANALISTA DE DADOS",
  core=["Qualidade e avaliação de dados","Análise exploratória de dados","Testes A/B e análise comparativa",
        "Dashboards (Power BI, Looker)","Data storytelling e visualização","Análise de produto e funil",
        "Colaboração multidisciplinar"],
  tech=["Consultas SQL","Python para análise de dados","HTML, CSS, JavaScript","Jira · Redmine · Google Sheets",
        "Documentação e produção de conteúdo","Plataformas EaD"],
  prof="Analista de Dados com sólida experiência em <b>tecnologia, educação e produção de games</b>, especializada em <b>qualidade de dados</b>, <b>comportamento de usuários</b> e <b>insights de produto</b>. Capacidade comprovada de traduzir dados complexos em decisões acionáveis com <b>SQL, Python, dashboards</b> e <b>data storytelling</b> — com certificações Google em <b>Data Analytics</b> e <b>Cloud Computing Foundations</b>, dois mestrados e vivência prática em pipelines de produção, fluxos de QA e sistemas voltados ao usuário em mobile, PC e console.",
  jobs1=[
   dict(t="Data Analyst", at="TELUS Digital", meta="2026 – atual · Montréal, Canadá", b=[
     "Realizo <b>avaliação de qualidade de dados</b> para consultas baseadas em mapas, garantindo <b>precisão</b> e <b>consistência</b> de informações geoespaciais.",
     "Analiso datasets de <b>POI</b> (Points of Interest), <b>SBS</b> (Search, Browse &amp; Services) e <b>áudio</b>, avaliando relevância de consultas, identificando discrepâncias e fornecendo feedback estruturado que melhora a qualidade da busca.",
     "Contribuo para a melhoria contínua dos <b>processos de qualidade de dados</b>, sustentando bases confiáveis para a tomada de decisão."]),
   dict(t="LQA Test Analyst", at="GlobalStep", meta="2025 – atual · Montréal, Canadá", b=[
     "Avalio a <b>qualidade de conteúdo de jogos</b> com foco em <b>consistência narrativa</b>, <b>precisão de localização</b>, usabilidade e funcionalidades voltadas ao jogador.",
     "Gero insights de qualidade para <b>títulos AA/AAA</b> — incluindo <b>Football Manager 26</b> e <b>Marvel Contest of Champions</b> — em mobile, PC e console, apoiando <b>decisões orientadas por dados</b> sobre a experiência do jogador.",
     "<b>Documento resultados</b> e acompanho issues em fluxos estruturados (Jira, Redmine, Google Sheets), colaborando com design, produção, QA e clientes."]),
   dict(t="Coordenadora Acadêmica &amp; Professora de TI", at="FMU, FAM, Impacta, UNICAP, UniBTA", meta="2018 – 2025 · São Paulo, Brasil", b=[
     "Conduzi o <b>monitoramento orientado por dados</b> de métricas de desempenho, engajamento e retenção acadêmica, atuando com equipes multidisciplinares na melhoria de resultados a partir de <b>KPIs</b>.",
     "Lecionei em mais de 30 disciplinas de <b>banco de dados</b>, <b>programação</b>, <b>análise de dados</b>, desenvolvimento de games e gestão de projetos.",
     "Produzi <b>relatórios, dashboards e documentação</b> de apoio à tomada de decisão estratégica."]),
  ],
  jobs2=[
   dict(t="Game &amp; Narrative Designer", at="Múltiplos estúdios", meta="2018 – 2023 · São Paulo, Brasil", b=[
     "Projetei <b>sistemas de progressão</b>, <b>loops de engajamento</b> e mecânicas de retenção orientadas por narrativa.",
     "Analisei <b>padrões de interação dos jogadores</b> para alinhar mecânicas ao comportamento do usuário, equilibrando gameplay e monetização com designers, desenvolvedores e artistas.",
     "Produzi <b>GDDs, whitepapers</b> e documentação de apoio a decisões de <b>design orientado por dados</b>."]),
   dict(t="Conversational Designer", at="Projetos selecionados", meta="2019 – 2020 · São Paulo, Brasil", b=[
     "Projetei e avaliei <b>fluxos conversacionais</b> e <b>árvores de decisão</b> para experiências digitais interativas, identificando pontos de atrito e melhorando o <b>engajamento do usuário</b>."]),
   dict(t="Agente Censitária", at="IBGE — Instituto Brasileiro de Geografia e Estatística", meta="2010 · São Paulo, Brasil", b=[
     "Coletei, validei e analisei dados populacionais para relatórios estatísticos oficiais, garantindo <b>precisão e consistência</b> em bases de larga escala."]),
  ],
  awards=["2º lugar — Uber Hack, 2019","Vencedora — Global Game Jam (Mimix VR), 2018",
          "1º lugar — Hackathon Cotidiano VR, 2017","1º lugar — Hack Engage, Campus Party Experience"],
  online=[("Portfólio","amandareznor.netlify.app/britto"),("Lattes","goo.gl/qd2oWR")],
  edu_keys=["ma_edu","ma_lit","spec_games","bsc_cs"],
 ),
 "fr": dict(
  role="Data Analyst",
  tag="Qualité des données · Analytique produit &amp; jeux · Data storytelling",
  foot="DATA ANALYST",
  core=["Qualité et évaluation des données","Analyse exploratoire de données","Tests A/B et analyse comparative",
        "Tableaux de bord (Power BI, Looker)","Data storytelling et visualisation","Analyse produit et d'entonnoir",
        "Travail interéquipes"],
  tech=["Requêtes SQL","Python pour l'analytique","HTML, CSS, JavaScript","Jira · Redmine · Google Sheets",
        "Documentation et contenu","Plateformes de formation en ligne"],
  prof="Data Analyst possédant une solide expérience en <b>technologie, éducation et production de jeux vidéo</b>, spécialisée en <b>qualité des données</b>, <b>comportement des utilisateurs</b> et <b>insights produit</b>. Capacité démontrée à transformer des données complexes en décisions concrètes grâce à <b>SQL, Python, aux tableaux de bord</b> et au <b>data storytelling</b> — appuyée par les certifications Google <b>Data Analytics</b> et <b>Cloud Computing Foundations</b>, deux maîtrises et une expérience pratique des pipelines de production, des flux d'AQ et des systèmes destinés aux utilisateurs sur mobile, PC et console.",
  jobs1=[
   dict(t="Data Analyst", at="TELUS Digital", meta="2026 – aujourd'hui · Montréal, Canada", b=[
     "Évaluation de la <b>qualité des données</b> pour des requêtes cartographiques, en assurant l'<b>exactitude</b> et la <b>cohérence</b> de l'information géospatiale.",
     "Analyse des ensembles de données <b>POI</b> (Points of Interest), <b>SBS</b> (Search, Browse &amp; Services) et <b>audio</b> : évaluation de la pertinence des requêtes, repérage des écarts et rétroaction structurée améliorant la qualité de la recherche.",
     "Contribution à l'amélioration continue des <b>processus de qualité des données</b>, au service de bases fiables pour la prise de décision."]),
   dict(t="LQA Test Analyst", at="GlobalStep", meta="2025 – aujourd'hui · Montréal, Canada", b=[
     "Évaluation de la <b>qualité du contenu de jeux</b> : <b>cohérence narrative</b>, <b>exactitude de la localisation</b>, utilisabilité et fonctionnalités destinées aux joueurs.",
     "Production d'insights qualité pour des <b>titres AA/AAA</b> — dont <b>Football Manager 26</b> et <b>Marvel Contest of Champions</b> — sur mobile, PC et console, à l'appui de <b>décisions guidées par les données</b> sur l'expérience joueur.",
     "<b>Documentation des constats</b> et suivi des anomalies dans des flux structurés (Jira, Redmine, Google Sheets), en collaboration avec le design, la production, l'AQ et les clients."]),
   dict(t="Academic Coordinator &amp; IT Professor", at="FMU, FAM, Impacta, UNICAP, UniBTA", meta="2018 – 2025 · São Paulo, Brésil", b=[
     "Pilotage d'un <b>suivi axé sur les données</b> des indicateurs de performance, d'engagement et de rétention académiques, avec des équipes multidisciplinaires et des <b>ICP</b>.",
     "Enseignement de plus de 30 cours : <b>bases de données</b>, <b>programmation</b>, <b>analytique</b>, développement de jeux et gestion de projet.",
     "Production de <b>rapports, tableaux de bord et documentation</b> à l'appui des décisions stratégiques."]),
  ],
  jobs2=[
   dict(t="Game &amp; Narrative Designer", at="Studios multiples", meta="2018 – 2023 · São Paulo, Brésil", b=[
     "Conception de <b>systèmes de progression</b>, de <b>boucles d'engagement</b> et de mécaniques de rétention portées par la narration.",
     "Analyse des <b>schémas d'interaction des joueurs</b> afin d'aligner les mécaniques de jeu sur les comportements, en équilibrant gameplay et monétisation avec les équipes de design, de développement et d'art.",
     "Production de <b>GDD, livres blancs</b> et documentation à l'appui de décisions de <b>design guidé par les données</b>."]),
   dict(t="Conversational Designer", at="Projets sélectionnés", meta="2019 – 2020 · São Paulo, Brésil", b=[
     "Conception et évaluation de <b>parcours conversationnels</b> et d'<b>arbres de décision</b> pour des expériences numériques interactives : réduction des frictions et amélioration de l'<b>engagement</b>."]),
   dict(t="Census Agent", at="IBGE — Institut brésilien de géographie et de statistique", meta="2010 · São Paulo, Brésil", b=[
     "Collecte, validation et analyse de données démographiques pour des rapports statistiques officiels, en garantissant <b>exactitude et cohérence</b> sur de grands ensembles de données."]),
  ],
  awards=["2<sup>e</sup> place — Uber Hack, 2019","Gagnante — Global Game Jam (Mimix VR), 2018",
          "1<sup>re</sup> place — Hackathon Cotidiano VR, 2017","1<sup>re</sup> place — Hack Engage, Campus Party Experience"],
  online=[("Portfolio","amandareznor.netlify.app/britto"),("Lattes","goo.gl/qd2oWR")],
  edu_keys=["ma_edu","ma_lit","spec_games","bsc_cs"],
 ),
}

# =============================================================================
# PROFILE B — GAMES: NARRATIVE DESIGN & LQA
# =============================================================================
GAMES = {
 "en": dict(
  role="Narrative Designer · LQA Analyst",
  tag="Game Writing · Localization QA · Worldbuilding &amp; Documentation",
  foot="NARRATIVE DESIGN &amp; LQA",
  core=["Narrative design &amp; game writing","Bilingual scripting (EN/PT)","Worldbuilding, lore &amp; GDDs",
        "LQA &amp; compliance testing","Localization quality","Regression &amp; ad hoc testing",
        "Cross-functional collaboration"],
  tech=["Unity · Twine · RPG Maker · Roblox Studio","Jira · Redmine · TestRail","HTML, CSS, JavaScript",
        "SQL, Python","Pitch bibles · GDDs · whitepapers","Hybrid test setups (Parsec, RDP, dev kits)"],
  prof="Narrative Designer and LQA Analyst bridging <b>game writing</b> and <b>quality assurance</b>. Author of bilingual scripts, lore, and GDDs for <b>award-recognized titles</b> (<b>Sleeping Dragon</b>, <b>Bedtime Fright</b>) and quality analyst on <b>AA/AAA productions</b> such as <b>Football Manager 26</b> and <b>Marvel Contest of Champions</b>. Published author — 2 books, 25+ short stories, 30+ anthologies — bringing a writer's eye to <b>localization, consistency, and player-facing text</b> across PC, console, and mobile.",
  jobs1=[
   dict(t="LQA Test Analyst", at="GlobalStep", meta="2025 – present · Montréal, Canada", b=[
     "Test and evaluate game content for <b>narrative quality, grammar, translation accuracy, localization</b>, contextual consistency, and functionality.",
     "LQA and compliance testing for <b>AA/AAA titles</b> — <b>Football Manager 26</b>, <b>NBA Bounce</b>, <b>Marvel Contest of Champions</b> — for publishers and studios including <b>SEGA, Sports Interactive, Outright Games, and Kabam</b>.",
     "Cross-platform coverage (Steam, PS5, Xbox, Switch, Netflix, iOS/Android): <b>point reviews, ad hoc, and full regression cycles</b>.",
     "Document results and track issues via <b>Jira, Redmine, and Google Sheets</b>; maintain internal databases (OTS, ORDB) supporting test coverage and compliance."]),
   dict(t="Narrative Designer", at="Vermillion — Sleeping Dragon", meta="2020 – present · São Paulo, Brazil", b=[
     "Developed the game's universe: <b>bilingual lore (PT/EN)</b>, dialogues, character catchphrases, maps, item tables, and NPC descriptions tied to gameplay mechanics.",
     "Produced the <b>Pitch Bible, GDD</b>, marketing articles, and a <b>ten-chapter book</b> set in the game's universe.",
     "Title selected for <b>Tokyo Game Show 2023</b>; released on <b>Steam</b>."]),
  ],
  jobs2=[
   dict(t="Narrative Designer", at="REVstudio — Bedtime Fright", meta="2018 · São Paulo, Brazil", b=[
     "Wrote the <b>bilingual script</b> and designed the <b>symbology system</b> for a psychological tale about the origin of a child's fear of the dark; authored a <b>children's book</b> based on the game's story.",
     "<b>SBGames 2018</b> · Finalist, <b>BIG Festival 2019</b> · <b>Best Brazilian Game — Sesc Game Place 2021</b>."]),
   dict(t="Narrative Designer", at="Lighthouse — Down Below", meta="2022 · remote", b=[
     "Web3 / P2E project: <b>bilingual lore, whitepaper, and GDD</b> documentation, character design, and weekly content for site and marketing."]),
   dict(t="Game Development Professor", at="College of Technology Impacta", meta="2020 – 2023 · São Paulo, Brazil", b=[
     "Taught <b>Game QA &amp; Testing</b> and game/mobile development environments, guiding hands-on <b>Unity</b> projects with production-oriented workflows, structured bug reporting, and feature validation."]),
   dict(t="Author &amp; Content Writer", at="Lua Nova Publishing", meta="2012 – present · São Paulo, Brazil", b=[
     "2 books and 25+ short stories published; featured at the <b>São Paulo International Book Biennial</b> (2012, 2016, 2022) and the <b>Rio de Janeiro Book Biennial</b> (2015); 100+ articles in magazines and newspapers."]),
  ],
  awards=["SBGames — 2018 &amp; 2019","Finalist — BIG Festival 2019 (two titles)","Best Brazilian Game — Sesc Game Place 2021",
          "Official selection — Tokyo Game Show 2023","Panorama Brasil — ProAC 2019","Winner — Global Game Jam (Mimix VR), 2018"],
  online=[("Portfolio","amandareznor.netlify.app"),("Steam","Sleeping Dragon"),("itch.io","revstudio.itch.io/bedtime-fright")],
  edu_keys=["spec_games","ma_lit","ma_edu","bsc_cs"],
 ),
 "pt": dict(
  role="Narrative Designer · LQA Analyst",
  tag="Escrita para games · LQA &amp; localização · Worldbuilding &amp; documentação",
  foot="NARRATIVE DESIGN &amp; LQA",
  core=["Narrative design e escrita para games","Roteirização bilíngue (EN/PT)","Worldbuilding, lore e GDDs",
        "Testes de LQA e compliance","Qualidade de localização","Testes de regressão e ad hoc",
        "Colaboração multidisciplinar"],
  tech=["Unity · Twine · RPG Maker · Roblox Studio","Jira · Redmine · TestRail","HTML, CSS, JavaScript",
        "SQL, Python","Pitch bibles · GDDs · whitepapers","Setups híbridos de teste (Parsec, RDP, dev kits)"],
  prof="Narrative Designer e LQA Analyst unindo <b>escrita para games</b> e <b>garantia de qualidade</b>. Autora de roteiros bilíngues, lore e GDDs de <b>títulos premiados</b> (<b>Sleeping Dragon</b>, <b>Bedtime Fright</b>) e analista de qualidade em <b>produções AA/AAA</b> como <b>Football Manager 26</b> e <b>Marvel Contest of Champions</b>. Escritora publicada — 2 livros, 25+ contos, 30+ antologias — com olhar de autora para <b>localização, consistência e texto voltado ao jogador</b> em PC, console e mobile.",
  jobs1=[
   dict(t="LQA Test Analyst", at="GlobalStep", meta="2025 – atual · Montréal, Canadá", b=[
     "Testo e avalio conteúdo de jogos quanto a <b>qualidade narrativa, gramática, precisão de tradução, localização</b>, consistência contextual e funcionalidade.",
     "Testes de LQA e compliance para <b>títulos AA/AAA</b> — <b>Football Manager 26</b>, <b>NBA Bounce</b>, <b>Marvel Contest of Champions</b> — para publishers e estúdios como <b>SEGA, Sports Interactive, Outright Games e Kabam</b>.",
     "Cobertura multiplataforma (Steam, PS5, Xbox, Switch, Netflix, iOS/Android): <b>point reviews, testes ad hoc e ciclos completos de regressão</b>.",
     "Documento resultados e acompanho issues via <b>Jira, Redmine e Google Sheets</b>; mantenho bases internas (OTS, ORDB) de apoio à cobertura de testes e compliance."]),
   dict(t="Narrative Designer", at="Vermillion — Sleeping Dragon", meta="2020 – atual · São Paulo, Brasil", b=[
     "Desenvolvi o universo do jogo: <b>lore bilíngue (PT/EN)</b>, diálogos, bordões de personagens, mapas, tabelas de itens e descrições de NPCs conectados às mecânicas.",
     "Produzi a <b>Pitch Bible, o GDD</b>, artigos de marketing e um <b>livro de dez capítulos</b> ambientado no universo do jogo.",
     "Título selecionado para a <b>Tokyo Game Show 2023</b>; lançado na <b>Steam</b>."]),
  ],
  jobs2=[
   dict(t="Narrative Designer", at="REVstudio — Bedtime Fright", meta="2018 · São Paulo, Brasil", b=[
     "Escrevi o <b>roteiro bilíngue</b> e projetei o <b>sistema de simbologia</b> de uma fábula psicológica sobre a origem do medo do escuro; autora do <b>livro infantil</b> baseado na história do jogo.",
     "<b>SBGames 2018</b> · Finalista do <b>BIG Festival 2019</b> · <b>Melhor Jogo Brasileiro — Sesc Game Place 2021</b>."]),
   dict(t="Narrative Designer", at="Lighthouse — Down Below", meta="2022 · remoto", b=[
     "Projeto Web3 / P2E: documentação de <b>lore bilíngue, whitepaper e GDD</b>, design de personagens e conteúdo semanal para site e marketing."]),
   dict(t="Professora de Desenvolvimento de Games", at="Faculdade de Tecnologia Impacta", meta="2020 – 2023 · São Paulo, Brasil", b=[
     "Lecionei <b>Game QA &amp; Testing</b> e ambientes de desenvolvimento de games e mobile, orientando projetos práticos em <b>Unity</b> com fluxos de produção, reporte estruturado de bugs e validação de features."]),
   dict(t="Autora &amp; Redatora", at="Lua Nova Editora", meta="2012 – atual · São Paulo, Brasil", b=[
     "2 livros e 25+ contos publicados; lançamentos na <b>Bienal Internacional do Livro de São Paulo</b> (2012, 2016, 2022) e na <b>Bienal do Livro do Rio</b> (2015); 100+ artigos em revistas e jornais."]),
  ],
  awards=["SBGames — 2018 &amp; 2019","Finalista — BIG Festival 2019 (dois títulos)","Melhor Jogo Brasileiro — Sesc Game Place 2021",
          "Seleção oficial — Tokyo Game Show 2023","Panorama Brasil — ProAC 2019","Vencedora — Global Game Jam (Mimix VR), 2018"],
  online=[("Portfólio","amandareznor.netlify.app"),("Steam","Sleeping Dragon"),("itch.io","revstudio.itch.io/bedtime-fright")],
  edu_keys=["spec_games","ma_lit","ma_edu","bsc_cs"],
 ),
 "fr": dict(
  role="Narrative Designer · LQA Analyst",
  tag="Écriture de jeux · AQ de localisation · Worldbuilding &amp; documentation",
  foot="NARRATIVE DESIGN &amp; LQA",
  core=["Design narratif et écriture de jeux","Scénarisation bilingue (EN/PT)","Worldbuilding, lore et GDD",
        "Tests LQA et de conformité","Qualité de la localisation","Tests de régression et ad hoc",
        "Travail interéquipes"],
  tech=["Unity · Twine · RPG Maker · Roblox Studio","Jira · Redmine · TestRail","HTML, CSS, JavaScript",
        "SQL, Python","Pitch bibles · GDD · livres blancs","Postes de test hybrides (Parsec, RDP, dev kits)"],
  prof="Narrative Designer et LQA Analyst à la jonction de l'<b>écriture de jeux</b> et de l'<b>assurance qualité</b>. Autrice de scénarios bilingues, de lore et de GDD pour des <b>titres primés</b> (<b>Sleeping Dragon</b>, <b>Bedtime Fright</b>) et analyste qualité sur des <b>productions AA/AAA</b> telles que <b>Football Manager 26</b> et <b>Marvel Contest of Champions</b>. Autrice publiée — 2 livres, 25+ nouvelles, 30+ anthologies — apportant un regard d'écrivaine à la <b>localisation, à la cohérence et aux textes destinés aux joueurs</b> sur PC, console et mobile.",
  jobs1=[
   dict(t="LQA Test Analyst", at="GlobalStep", meta="2025 – aujourd'hui · Montréal, Canada", b=[
     "Test et évaluation du contenu de jeux : <b>qualité narrative, grammaire, exactitude de la traduction, localisation</b>, cohérence contextuelle et fonctionnalité.",
     "Tests LQA et de conformité pour des <b>titres AA/AAA</b> — <b>Football Manager 26</b>, <b>NBA Bounce</b>, <b>Marvel Contest of Champions</b> — pour des éditeurs et studios dont <b>SEGA, Sports Interactive, Outright Games et Kabam</b>.",
     "Couverture multiplateforme (Steam, PS5, Xbox, Switch, Netflix, iOS/Android) : <b>revues ciblées, tests ad hoc et cycles complets de régression</b>.",
     "Documentation des résultats et suivi des anomalies via <b>Jira, Redmine et Google Sheets</b>; tenue de bases internes (OTS, ORDB) pour la couverture de tests et la conformité."]),
   dict(t="Narrative Designer", at="Vermillion — Sleeping Dragon", meta="2020 – aujourd'hui · São Paulo, Brésil", b=[
     "Développement de l'univers du jeu : <b>lore bilingue (PT/EN)</b>, dialogues, répliques de personnages, cartes, tables d'objets et descriptions de PNJ liées aux mécaniques.",
     "Production de la <b>Pitch Bible, du GDD</b>, d'articles marketing et d'un <b>livre en dix chapitres</b> situé dans l'univers du jeu.",
     "Titre sélectionné au <b>Tokyo Game Show 2023</b>; paru sur <b>Steam</b>."]),
  ],
  jobs2=[
   dict(t="Narrative Designer", at="REVstudio — Bedtime Fright", meta="2018 · São Paulo, Brésil", b=[
     "Écriture du <b>scénario bilingue</b> et conception du <b>système de symbologie</b> d'un conte psychologique sur l'origine de la peur du noir; autrice du <b>livre jeunesse</b> tiré de l'histoire du jeu.",
     "<b>SBGames 2018</b> · Finaliste — <b>BIG Festival 2019</b> · <b>Meilleur jeu brésilien — Sesc Game Place 2021</b>."]),
   dict(t="Narrative Designer", at="Lighthouse — Down Below", meta="2022 · à distance", b=[
     "Projet Web3 / P2E : documentation de <b>lore bilingue, livre blanc et GDD</b>, design de personnages et contenu hebdomadaire pour le site et le marketing."]),
   dict(t="Game Development Professor", at="Faculté de technologie Impacta", meta="2020 – 2023 · São Paulo, Brésil", b=[
     "Enseignement de <b>Game QA &amp; Testing</b> et des environnements de développement jeu/mobile : projets pratiques sous <b>Unity</b>, flux orientés production, rapports de bogues structurés et validation de fonctionnalités."]),
   dict(t="Author &amp; Content Writer", at="Lua Nova (maison d'édition)", meta="2012 – aujourd'hui · São Paulo, Brésil", b=[
     "2 livres et 25+ nouvelles publiés; lancements à la <b>Biennale internationale du livre de São Paulo</b> (2012, 2016, 2022) et à la <b>Biennale du livre de Rio</b> (2015); 100+ articles en presse et magazines."]),
  ],
  awards=["SBGames — 2018 &amp; 2019","Finaliste — BIG Festival 2019 (deux titres)","Meilleur jeu brésilien — Sesc Game Place 2021",
          "Sélection officielle — Tokyo Game Show 2023","Panorama Brasil — ProAC 2019","Gagnante — Global Game Jam (Mimix VR), 2018"],
  online=[("Portfolio","amandareznor.netlify.app"),("Steam","Sleeping Dragon"),("itch.io","revstudio.itch.io/bedtime-fright")],
  edu_keys=["spec_games","ma_lit","ma_edu","bsc_cs"],
 ),
}

# =============================================================================
# PROFILE C — EDUCATION: TEACHING & ACADEMIC MANAGEMENT
# =============================================================================
EDUCATION = {
 "en": dict(
  role="University Professor &amp; Academic Coordinator",
  tag="Information Technology · Higher Education · Academic Management",
  foot="EDUCATION &amp; MANAGEMENT",
  core_label="general",
  core=["Project &amp; team management","Curriculum &amp; instructional design","Academic documentation (PDI, PPC, teaching plans)",
        "Strong written &amp; verbal communication","Conflict mediation","Critical analysis &amp; problem-solving"],
  tech=["E-learning platforms (Blackboard, Canvas, Moodle, AVA)","Instructional design","Data analysis",
        "HTML, CSS, JavaScript","SQL, Python","Documentation &amp; content production"],
  prof="University professor with <b>seven years of experience in higher education</b> and two Master's degrees (<b>Education</b> and <b>Literature</b>). Taught <b>30+ IT courses</b> and served as <b>Academic Coordinator</b> at FAM and FMU (São Paulo, Brazil). <b>Four years as an ad hoc reviewer for INEP</b>, the Brazilian Ministry of Education's evaluation agency, and over a decade producing academic and instructional content — <b>100+ books and 30+ technical articles</b> across e-books, scripts, question banks, and teaching plans.",
  jobs1=[
   dict(t="Professor &amp; Academic Coordinator", at="FMU, FAM, Impacta, UNICAP, UniBTA", meta="Jan 2018 – Jan 2025 · São Paulo, Brazil", b=[
     "Taught <b>30+ IT courses</b>, including front-end and back-end programming, <b>databases</b>, game development, and project management — with full ownership of content production, learning assessment, and academic documentation.",
     "As <b>Coordinator</b> (FAM) and assistant coordinator (FMU), led IT programs with a <b>multidisciplinary team</b>: weekly metrics reviews, <b>monitoring and control of results</b>, and support to partners and students.",
     "Reviewed, produced, and updated institutional documentation — <b>PDI, PPCs, and teaching plans</b> — and mediated between departments (registrar, pedagogy, instructional design, IT).",
     "Contributed to tutoring, research, and extension projects alongside regular teaching."]),
   dict(t="Ad hoc Reviewer", at="INEP — Brazilian Ministry of Education", meta="Jul 2020 – Dec 2023 · Brazil", b=[
     "Served on <b>evaluation committees</b> designated by INEP, providing technical and pedagogical collaboration in the permanent process of <b>evaluation, follow-up, and improvement of national higher-education standards</b> in Information Technology."]),
  ],
  jobs2=[
   dict(t="Content Specialist", at="VG Educational", meta="Oct 2019 – Mar 2023 · São Paulo, Brazil", b=[
     "Validated and produced <b>didactic content for higher education</b> across Brazilian institutions: <b>30+ productions</b> including e-books, class-recording scripts, cases, activities, question banks, and teaching plans for IT, digital games, design, marketing, and communication."]),
   dict(t="Data Analyst", at="TELUS Digital", meta="2026 – present · Montréal, Canada", b=[
     "Data quality assessment and analysis for map-based queries, ensuring accuracy and consistency of geospatial information."]),
   dict(t="LQA Test Analyst", at="GlobalStep", meta="2025 – present · Montréal, Canada", b=[
     "Quality evaluation of game content — narrative, localization, and functionality — for AA/AAA titles across PC, console, and mobile."]),
  ],
  awards=["4º SAPIÊNCIA — National Seminar of Scientific Initiation: organization","2<sup>nd</sup> place — Uber Hack, 2019",
          "Winner — Global Game Jam (Mimix VR), 2018","1<sup>st</sup> place — Hackathon Cotidiano VR, 2017"],
  online=[("Portfolio","amandareznor.netlify.app/britto"),("Lattes","goo.gl/qd2oWR")],
  edu_keys=["ma_lit","ma_edu","spec_games","bsc_cs","tech_web"],
  qual=("Data Engineering, Data Science &amp; Business Intelligence — São Judas University",
        "Oct – Dec 2019 · 100-hour extension course: Python for data analysis, machine-learning algorithm design, clustering, Spark, and Power BI, with a final project on the Olist database (Kaggle)."),
 ),
 "pt": dict(
  role="Professora Universitária &amp; Coordenadora Acadêmica",
  tag="Tecnologia da Informação · Ensino Superior · Gestão Acadêmica",
  foot="EDUCAÇÃO &amp; GESTÃO",
  core_label="general",
  core=["Gestão de projetos e de equipes","Currículo e design instrucional","Documentação acadêmica (PDI, PPC, Planos de Ensino)",
        "Comunicação verbal e escrita","Mediação de conflitos","Análise crítica e resolução de problemas"],
  tech=["Plataformas EaD (Blackboard, Canvas, Moodle, AVA)","Design instrucional","Análise de dados",
        "HTML, CSS, JavaScript","SQL, Python","Documentação e produção de conteúdo"],
  prof="Professora universitária com <b>sete anos de experiência no Ensino Superior</b> e dois mestrados (<b>Educação</b> e <b>Letras</b>). Lecionei em <b>mais de 30 disciplinas de TI</b> e atuei como <b>Coordenadora Acadêmica</b> na FAM e na FMU (São Paulo). <b>Quatro anos como avaliadora ad hoc do INEP/MEC</b> e mais de uma década de produção de conteúdo acadêmico e instrucional — <b>100+ livros e 30+ artigos técnicos</b>, entre e-books, roteiros, bancos de questões e planos de ensino.",
  jobs1=[
   dict(t="Professora &amp; Coordenadora Acadêmica", at="FMU, FAM, Impacta, UNICAP, UniBTA", meta="Jan 2018 – Jan 2025 · São Paulo, Brasil", b=[
     "Lecionei em <b>mais de 30 disciplinas de TI</b> — programação front-end e back-end, <b>banco de dados</b>, desenvolvimento de games e gestão de projetos — com responsabilidade integral por produção de conteúdo, acompanhamento da aprendizagem e documentação acadêmica.",
     "Como <b>Coordenadora</b> (FAM) e auxiliar de coordenação (FMU), conduzi cursos de TI com <b>equipe multidisciplinar</b>: reuniões semanais de métricas, <b>monitoramento e controle de resultados</b> e suporte a parceiros e discentes.",
     "Revisei, produzi e atualizei documentação institucional — <b>PDI, PPCs e Planos de Ensino</b> — e mediei conflitos entre departamentos (Secretaria, equipe pedagógica, Design Instrucional e TI).",
     "Atuei em projetos de tutoria, pesquisa e extensão em paralelo à docência."]),
   dict(t="Avaliadora ad hoc", at="INEP — Ministério da Educação", meta="Jul 2020 – Dez 2023 · Brasil", b=[
     "Participei de <b>comissões de avaliação</b> designadas pelo INEP, com colaboração técnica e pedagógica no processo permanente de <b>avaliação, acompanhamento e melhoria dos padrões nacionais do Ensino Superior</b> em Tecnologia da Informação."]),
  ],
  jobs2=[
   dict(t="Especialista de Conteúdo", at="VG Educacional", meta="Out 2019 – Mar 2023 · São Paulo, Brasil", b=[
     "Validação e produção de <b>conteúdo didático para o Ensino Superior</b> de diferentes instituições brasileiras: <b>30+ produções</b> entre e-books, roteiros de gravação de aulas, cases, atividades, bancos de questões e planos de ensino para TI, jogos digitais, design, marketing e comunicação."]),
   dict(t="Data Analyst", at="TELUS Digital", meta="2026 – atual · Montréal, Canadá", b=[
     "Avaliação e análise de qualidade de dados para consultas baseadas em mapas, garantindo precisão e consistência de informações geoespaciais."]),
   dict(t="LQA Test Analyst", at="GlobalStep", meta="2025 – atual · Montréal, Canadá", b=[
     "Avaliação de qualidade de conteúdo de jogos — narrativa, localização e funcionalidade — em títulos AA/AAA para PC, console e mobile."]),
  ],
  awards=["4º SAPIÊNCIA — Seminário Nacional de Iniciação Científica: organização","2º lugar — Uber Hack, 2019",
          "Vencedora — Global Game Jam (Mimix VR), 2018","1º lugar — Hackathon Cotidiano VR, 2017"],
  online=[("Portfólio","amandareznor.netlify.app/britto"),("Lattes","goo.gl/qd2oWR")],
  edu_keys=["ma_lit","ma_edu","spec_games","bsc_cs","tech_web"],
  qual=("Engenharia de Dados, Data Science &amp; Business Intelligence — Universidade São Judas",
        "Out – Dez 2019 · Curso de extensão de 100 horas: Python para análise de dados, algoritmos de machine learning, clustering, Spark e Power BI, com projeto final sobre a base Olist (Kaggle)."),
 ),
 "fr": dict(
  role="University Professor &amp; Academic Coordinator",
  tag="Technologies de l'information · Enseignement supérieur · Gestion académique",
  foot="ÉDUCATION &amp; GESTION",
  core_label="general",
  core=["Gestion de projets et d'équipes","Programmes et design pédagogique","Documentation académique (PDI, PPC)",
        "Communication écrite et orale","Médiation de conflits","Résolution de problèmes"],
  tech=["Blackboard, Canvas, Moodle, AVA","Design pédagogique","Analyse de données",
        "HTML, CSS, JavaScript","SQL, Python","Documentation et production de contenu"],
  prof="Professeure d'université comptant <b>sept années d'expérience en enseignement supérieur</b> et deux maîtrises (<b>éducation</b> et <b>lettres</b>). Enseignement de <b>plus de 30 cours en TI</b> et rôle de <b>coordonnatrice académique</b> à la FAM et à la FMU (São Paulo, Brésil). <b>Quatre ans comme évaluatrice ad hoc pour l'INEP</b>, l'agence d'évaluation du ministère brésilien de l'Éducation, et plus d'une décennie de production de contenu académique et pédagogique — <b>100+ livres et 30+ articles techniques</b> : livres numériques, scénarios de cours, banques de questions et plans de cours.",
  jobs1=[
   dict(t="Professor &amp; Academic Coordinator", at="FMU, FAM, Impacta, UNICAP, UniBTA", meta="janv. 2018 – janv. 2025 · São Paulo, Brésil", b=[
     "Enseignement de <b>plus de 30 cours en TI</b> — programmation front-end et back-end, <b>bases de données</b>, développement de jeux et gestion de projet — avec pleine responsabilité de la production de contenu, du suivi des apprentissages et de la documentation académique.",
     "À titre de <b>coordonnatrice</b> (FAM) et de coordonnatrice adjointe (FMU), pilotage de programmes de TI avec une <b>équipe multidisciplinaire</b> : revues hebdomadaires d'indicateurs, <b>suivi et contrôle des résultats</b>, soutien aux partenaires et aux étudiants.",
     "Révision, production et mise à jour de la documentation institutionnelle — <b>PDI, PPC et plans de cours</b> — et médiation entre les services (registrariat, pédagogie, design pédagogique, TI).",
     "Participation à des projets de tutorat, de recherche et de rayonnement en parallèle de l'enseignement."]),
   dict(t="Ad hoc Reviewer", at="INEP — ministère brésilien de l'Éducation", meta="juill. 2020 – déc. 2023 · Brésil", b=[
     "Participation à des <b>comités d'évaluation</b> désignés par l'INEP : collaboration technique et pédagogique au processus permanent d'<b>évaluation, de suivi et d'amélioration des normes nationales de l'enseignement supérieur</b> en technologies de l'information."]),
  ],
  jobs2=[
   dict(t="Content Specialist", at="VG Educational", meta="oct. 2019 – mars 2023 · São Paulo, Brésil", b=[
     "Validation et production de <b>contenu didactique pour l'enseignement supérieur</b> de diverses institutions brésiliennes : <b>30+ productions</b> — livres numériques, scénarios d'enregistrement de cours, études de cas, activités, banques de questions et plans de cours en TI, jeux numériques, design, marketing et communication."]),
   dict(t="Data Analyst", at="TELUS Digital", meta="2026 – aujourd'hui · Montréal, Canada", b=[
     "Évaluation et analyse de la qualité des données pour des requêtes cartographiques, en assurant l'exactitude et la cohérence de l'information géospatiale."]),
   dict(t="LQA Test Analyst", at="GlobalStep", meta="2025 – aujourd'hui · Montréal, Canada", b=[
     "Évaluation de la qualité du contenu de jeux — narration, localisation et fonctionnalité — sur des titres AA/AAA (PC, console, mobile)."]),
  ],
  awards=["4º SAPIÊNCIA — Séminaire national d'initiation scientifique : organisation","2<sup>e</sup> place — Uber Hack, 2019",
          "Gagnante — Global Game Jam (Mimix VR), 2018","1<sup>re</sup> place — Hackathon Cotidiano VR, 2017"],
  online=[("Portfolio","amandareznor.netlify.app/britto"),("Lattes","goo.gl/qd2oWR")],
  edu_keys=["ma_lit","ma_edu","spec_games","bsc_cs","tech_web"],
  qual=("Data Engineering, Data Science &amp; Business Intelligence — Université São Judas",
        "oct. – déc. 2019 · Cours d'extension de 100 heures : Python pour l'analyse de données, conception d'algorithmes d'apprentissage automatique, clustering, Spark et Power BI; projet final sur la base Olist (Kaggle)."),
 ),
}

PROFILES = {"data-analyst": DATA_ANALYST, "games": GAMES, "education": EDUCATION}
