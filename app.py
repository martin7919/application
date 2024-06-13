import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


st.title("Bizottság választó")
st.write("Válaszolj néhány kérdésre, hogy megtudd, melyik a szakkollégium melyik bizottsága a leginkább testhezálló a számodra.")

# Check if the form is opened
if 'show_form' not in st.session_state:
    st.session_state.show_form = False

# Button to show/hide the form
if st.button("Kezdjük!") or st.session_state.show_form:
    st.session_state.show_form = True
    # Subheader and Questions
    st.subheader('Kérdések:')
    st.write("Ahol csúszka van, az állítással való egyetértésedet kell kinyilvánítanod.")

    piller = st.radio("Mit tartasz a szakkollégiumiság legfőbb pillérének?",["Közösség", "Szakma", "Társadalmi felelősségvállalás"])
    kepviselo = st.radio("Kinek kell a díjas előadáson kint ülnie?",["DB titkár", "SZMT elnök", "Változó"])
    intro_extro = st.slider("Extrovertált személyiségnek tartom magam.", 0, 100, 50)
    kozosseg_szakma = st.slider("A szakmai kiválóság sokkal fontosabb, mint a közösség magjában lenni.", 0, 100, 50)
    tarsifel = st.slider("A társadalmi felelősségvállalás a szívügyem.", 0, 100, 50)
    operativ_strategia = st.slider("A stratégiaalkotás jobban lázba hoz, mint az operatív munka.", 0, 100, 50)
    kulkapcs = st.slider("A kollégium nem csak magában értelmezendő - fontosak a külkapcsolatok.", 0, 100, 50)
    tartalom_formatum = st.slider("A formátum legalább olyan fontos, mint a tartalom.", 0, 100, 50)
    korai_kesoi = st.slider("Nem okoznak gondot a hajnalig tartó megbeszélések.", 0, 100, 50)
    felnottek = st.slider("Szeretem, ha tapasztalt felnőttekkel dolgozhatok együtt.", 0, 100, 50)
    elmeleti_gyakorlati = st.slider("A kollégiumban nem csak filozofálgatnunk, de gazdálkodunk is tudni kell.", 0, 100, 50)
    proaktivitas = st.slider("Nem zavar, ha egy hirtelen kolis probléma esetén rögtön a tettek mezejére kell lépnem.", 0, 100, 50)
    kultevekenyseg = st.slider("A kollégium határai nem a kapuig tartanak.", 0, 100, 50)
    befele_kifele = st.slider("Fontos, hogy többet mutassunk magunkból a külvilág felé.", 0, 100, 50)

    if st.button("Mutasd az eredményt!"):
        committe_profiles = {
            "Diákbizottság": {
                "piller": "Közösség",
                "kepviselo": "DB titkár",
                "intro_extro": 100,
                "kozosseg_szakma": 20,
                "tarsifel": 60,
                "operativ_strategia": 100,
                "kulkapcs": 60,
                "tartalom_formatum": 20,
                "korai_kesoi": 100,
                "felnottek": 40,
                "elmeleti_gyakorlati": 0,
                "proaktivitas": 80,
                "kultevekenyseg": 60,
                "befele_kifele": 40
            },
            "SZMT": {
                "piller": "Szakma",
                "kepviselo": "SZMT elnök",
                "intro_extro": 20,
                "kozosseg_szakma": 100,
                "tarsifel": 0,
                "operativ_strategia": 40,
                "kulkapcs": 40,
                "tartalom_formatum": 80,
                "korai_kesoi": 40,
                "felnottek": 20,
                "elmeleti_gyakorlati": 80,
                "proaktivitas": 60,
                "kultevekenyseg": 40,
                "befele_kifele": 60
            },
            "SZKTP": {
                "piller": "Társadalmi felelősségvállalás",
                "kepviselo": "Változó",
                "intro_extro": 40,
                "kozosseg_szakma": 60,
                "tarsifel": 100,
                "operativ_strategia": 60,
                "kulkapcs": 80,
                "tartalom_formatum": 0,
                "korai_kesoi": 60,
                "felnottek": 60,
                "elmeleti_gyakorlati": 40,
                "proaktivitas": 0,
                "kultevekenyseg": 100,
                "befele_kifele": 80
            },
            "PIMPS": {
                "piller": "Szakma",
                "kepviselo": "DB titkár",
                "intro_extro": 0,
                "kozosseg_szakma": 80,
                "tarsifel": 20,
                "operativ_strategia": 0,
                "kulkapcs": 20,
                "tartalom_formatum": 40,
                "korai_kesoi": 20,
                "felnottek": 100,
                "elmeleti_gyakorlati": 100,
                "proaktivitas": 20,
                "kultevekenyseg": 20,
                "befele_kifele": 0
            },
            "ÉPTEST": {
                "piller": "Közösség",
                "kepviselo": "DB titkár",
                "intro_extro": 60,
                "kozosseg_szakma": 0,
                "tarsifel": 80,
                "operativ_strategia": 20,
                "kulkapcs": 0,
                "tartalom_formatum": 60,
                "korai_kesoi": 80,
                "felnottek": 80,
                "elmeleti_gyakorlati": 60,
                "proaktivitas": 100,
                "kultevekenyseg": 0,
                "befele_kifele": 20
            },
            "KomKol": {
                "piller": "Közösség",
                "kepviselo": "Változó",
                "intro_extro": 80,
                "kozosseg_szakma": 40,
                "tarsifel": 40,
                "operativ_strategia": 80,
                "kulkapcs": 100,
                "tartalom_formatum": 100,
                "korai_kesoi": 0,
                "felnottek": 0,
                "elmeleti_gyakorlati": 20,
                "proaktivitas": 40,
                "kultevekenyseg": 80,
                "befele_kifele": 100
            }
        }

        user_responses = np.array([
            intro_extro,
            kozosseg_szakma,
            tarsifel,
            operativ_strategia,
            kulkapcs,
            tartalom_formatum,
            korai_kesoi,
            felnottek,
            elmeleti_gyakorlati,
            proaktivitas,
            kultevekenyseg,
            befele_kifele
        ])

        #Algoritmus

        def calculate_distance(user_responses, committe_profile, piller, kepviselo):
            profile_values = np.array(list(committe_profile.values())[2:])
            distance = np.linalg.norm(user_responses - profile_values)
            
            if committe_profile["piller"] != piller:
                distance += 10
            if committe_profile["kepviselo"] != kepviselo:
                distance += 10
            
            return distance

        # Spider plot
        committe_distances = {}
        for committe, profile in committe_profiles.items():
            committe_distances[committe] = calculate_distance(user_responses, profile, piller, kepviselo)

        recommended_committe = min(committe_distances, key=committe_distances.get)
        st.markdown(f"## Válaszaid alapján hozzád a(z) **{recommended_committe}** illik leginkább, de itt láthatod a teljes eredményt:")

        committee_names = list(committe_distances.keys())
        distances = list(committe_distances.values())

        max_distance = 480

        inverted_distances = [max_distance - d for d in distances]

        fig, ax = plt.subplots(figsize=(5, 5), subplot_kw=dict(polar=True))
        theta = np.linspace(0, 2 * np.pi, len(committee_names), endpoint=False).tolist()
        inverted_distances += inverted_distances[:1]
        theta += theta[:1]
        ax.fill(theta, inverted_distances, 'g', alpha=0.2)
        ax.plot(theta, inverted_distances, color='g', linewidth=0.3)
        ax.set_ylim(0, max_distance)
        ax.set_xticks(theta[:-1])
        ax.set_xticklabels(committee_names)
        ax.tick_params(axis='x', labelsize=8)

        ax.set_yticklabels([])

        st.pyplot(fig)
