import pandas as pd
import plot_likert as plot_likert
import numpy as np
import matplotlib.pyplot as plt
import pylab as p
import streamlit as st

st.set_option('deprecation.showPyplotGlobalUse', False)

st.title('Visualisierung der Seminarevaluation')
st.text('Hier kannst du deine Seminarevaluation in Histogrammen anzeigen lassen')

uploaded_file = st.file_uploader('Hier die CSV-Datei aus dem Moodle-Kurs hochladen:')

if uploaded_file:
    df2 = pd.read_csv(uploaded_file)
    df2 = df2.replace('Nicht beantwortbar', np.NaN)
    scale = ['Trifft nicht zu', 'Trifft eher nicht zu', 'Teils/Teils', 'Trifft eher zu', 'Trifft voll und ganz zu']
    data_1 = df2[['1.1) Aufbau und Gliederung der Veranstaltung waren klar. ',
                  '1.2) Die Lehrveranstaltung hat mir viele neue inhaltliche Erkenntnisse gebracht.',
                  '1.3) Die Leistungsanforderungen wurden transparent dargelegt.',
                  '1.4) Die zu Beginn der Veranstaltung beschriebenen Lernziele wurden bisher erfüllt.',
                  '1.5) Die veranstaltungsbegleitenden Materialien erleichterten das Verständnis des Seminarinhalts/-stoffes.',
                  '1.6) Die digitalen Formate unterstützten den Lernprozess.']]
    data_2 = df2[['2.1) Die/der Dozent_in war es wichtig, dass die Studierenden etwas lernen',
                  '2.2) Die Lehrveranstaltung/Aufgaben trugen zum Verständnis von Theorie und Praxis bei.',
                  '2.3) Die Lerninhalte wurden mit Beispielen aus der Praxis veranschaulicht.',
                  '2.4) Die/Der Dozent_in folgte immer einem klar nachvollziehbarem roten Faden.',
                  '2.5) Die/Der Dozent_in stellte Verbindungen zu bereits besprochenem Stoff aus der Veranstaltung her.',
                  '2.6) Die/Der Dozent_in hat klar und deutlich gesprochen.',
                  '2.7) Die/Der Dozent_in antwortete verständlich auf die Fragen der Studierenden.',
                  '2.8) Die Aufgaben trugen zum Verständnis der Veranstaltung bei.',
                  '2.9) Die Lehrformen waren abwechslungsreich gestaltet.']]
    data_3 = df2[[
        '3.1 Die/der Dozent_in schuf eine Atmosphäre, in der Studierende Fragen und Kommentare zum Stoff ohne Scheu äußerten.',
        '3.2) Die/der Dozent_in trug zu einem respektvollen Lehr-Lernklima in der Veranstaltung bei.',
        '3.3) Die Studierenden trugen zu einem respektvollen Lehr-Lernklima in der Veranstaltung bei.',
        '3.4) Die Studierenden wurden zur kritischen Auseinandersetzung mit den Inhalten der Veranstaltung angeregt.']]
    data_4 = df2[[
        '4.1) Die/Der Dozent_in achtete darauf, dass in ihren Ausführungen Menschen nicht in stereotypen/diskriminierenden Bildern beschrieben wurden.',
        '4.2) Wenn Inhalte erläutert wurden, wurde die Vielfalt der Erfahrungen der Studierenden berücksichtigt.']]

    #st.write(df2.head())

    plot_likert.plot_likert(data_1, scale, plot_percentage=True,
                            bar_labels=True, bar_labels_color="snow",
                            colors=plot_likert.colors.default_with_darker_neutral, figsize=(8, 11))

    st.pyplot()

    plot_likert.plot_likert(data_2, scale, plot_percentage=True, bar_labels=True, bar_labels_color="snow",
                            colors=plot_likert.colors.default_with_darker_neutral, figsize=(8, 13))

    st.pyplot()

    plot_likert.plot_likert(data_3, scale, plot_percentage=True,
                            bar_labels=True, bar_labels_color="snow",
                            colors=plot_likert.colors.default_with_darker_neutral, figsize=(8, 6))

    st.pyplot()

    plot_likert.plot_likert(data_4, scale, plot_percentage=True,
                           bar_labels=True, bar_labels_color="snow",
                           colors=plot_likert.colors.default_with_darker_neutral, figsize=(8, 3))

    st.pyplot()

    st.markdown('## Was hat Ihnen an der Lehrveranstaltung besonders gut gefallen?')

    df3 = df2['Was hat Ihnen an der Lehrveranstaltung besonders gut gefallen (Stichpunkte)'].dropna()
    st.markdown(df3.values)

    df4 = df2['Welche Verbesserungsvorschläge haben Sie? (Stichpunkte)'].dropna()

    st.markdown('## Welche Verbesserungsvorschläge haben Sie?')

    st.markdown(df4.values)


