import streamlit as st
import pandas as pd

st.set_page_config(page_title="Textile Fiber Hub", page_icon="🧵", layout="wide")

FIBERS = {
    "Cotton": {
        "category": "Natural • Cellulosic",
        "source": "Cotton plant seed hairs",
        "composition": "Mainly cellulose",
        "microstructure": "Long cellulose chains with crystalline and amorphous regions. The fiber has a twisted, ribbon-like form and a lumen.",
        "macrostructure": "Natural staple fiber with a soft, slightly twisted appearance.",
        "properties": ["Good moisture absorbency", "Comfortable", "Good dye affinity", "Moderate strength", "Low elasticity"],
        "uses": ["Shirts", "Bed sheets", "Towels", "Denim", "Underwear"],
    },
    "Flax": {
        "category": "Natural • Cellulosic",
        "source": "Stem of the flax plant",
        "composition": "Mainly cellulose",
        "microstructure": "Cellulose chains are organized into crystalline and amorphous regions; technical fibers contain bundles of elementary fibers.",
        "macrostructure": "Natural bast staple fiber that is relatively stiff, strong, and smooth.",
        "properties": ["High strength", "Good absorbency", "Good heat conductivity", "Low elasticity", "Cool handle"],
        "uses": ["Linen clothing", "Table linen", "Bed linen", "Home textiles"],
    },
    "Jute": {
        "category": "Natural • Cellulosic",
        "source": "Stem of jute plants",
        "composition": "Cellulose, hemicellulose, and lignin",
        "microstructure": "Bast fiber bundles contain cellulose-rich regions with hemicellulose and lignin.",
        "macrostructure": "Coarse, strong natural bast fiber with a relatively rough handle.",
        "properties": ["Good strength", "Biodegradable", "Good moisture absorption", "Low elasticity", "Coarse handle"],
        "uses": ["Sacks", "Ropes", "Twine", "Carpets", "Geotextiles"],
    },
    "Wool": {
        "category": "Natural • Protein",
        "source": "Fleece of sheep and other wool-bearing animals",
        "composition": "Keratin protein",
        "microstructure": "Has a cuticle with overlapping scales, a cortex, and in some coarse fibers a medulla. The cortex contributes to crimp and fiber properties.",
        "macrostructure": "Natural crimped staple fiber with a scaly surface; resilient, warm, and bulky.",
        "properties": ["Good warmth", "Good resilience", "Moisture absorption", "Natural crimp", "Good insulation"],
        "uses": ["Suits", "Sweaters", "Blankets", "Carpets", "Winter clothing"],
    },
    "Silk": {
        "category": "Natural • Protein",
        "source": "Silkworm cocoon filament",
        "composition": "Fibroin with sericin as the main coating in raw silk",
        "microstructure": "Fibroin contains ordered crystalline regions associated with beta-sheet structures and less ordered regions.",
        "macrostructure": "Natural continuous filament that is fine, smooth, lustrous, and flexible.",
        "properties": ["High luster", "Good strength", "Smooth handle", "Good drape", "Moderate absorbency"],
        "uses": ["Dresses", "Scarves", "Ties", "Luxury fabrics", "Decorative textiles"],
    },
    "Rayon": {
        "category": "Man-made • Regenerated cellulosic",
        "source": "Cellulose regenerated into fiber form",
        "composition": "Regenerated cellulose",
        "microstructure": "Regenerated cellulose chains form crystalline and amorphous regions.",
        "macrostructure": "Produced as filament or staple fiber with controlled length, fineness, and cross-section.",
        "properties": ["Soft handle", "Good absorbency", "Good drape", "Good dyeability"],
        "uses": ["Dresses", "Shirts", "Linings", "Home textiles"],
    },
    "Polyester": {
        "category": "Man-made • Synthetic",
        "source": "Synthetic polymer feedstocks",
        "composition": "Polyester polymer, commonly PET",
        "microstructure": "Long polymer chains contain crystalline and amorphous regions; drawing can increase molecular orientation.",
        "macrostructure": "Produced as continuous filament or staple fiber with controlled fineness and cross-section.",
        "properties": ["High strength", "Good dimensional stability", "Low moisture absorbency", "Wrinkle resistance"],
        "uses": ["Sportswear", "Shirts", "Home textiles", "Industrial fabrics"],
    },
    "Nylon": {
        "category": "Man-made • Synthetic",
        "source": "Synthetic polyamide polymer",
        "composition": "Polyamide",
        "microstructure": "Polyamide chains form crystalline and amorphous regions, with hydrogen bonding contributing to molecular interactions.",
        "macrostructure": "Strong, flexible filament or staple fiber with controllable fineness.",
        "properties": ["High strength", "High abrasion resistance", "Good elasticity", "Lightweight"],
        "uses": ["Hosiery", "Sportswear", "Ropes", "Carpets"],
    },
    "Acrylic": {
        "category": "Man-made • Synthetic",
        "source": "Synthetic polymer based mainly on acrylonitrile",
        "composition": "Acrylic polymer, mainly polyacrylonitrile or related copolymers",
        "microstructure": "Polymer chains form ordered and less ordered regions; processing controls orientation and morphology.",
        "macrostructure": "Usually produced as staple fibers designed to imitate wool-like handle and appearance.",
        "properties": ["Lightweight", "Warm", "Good color retention", "Soft handle"],
        "uses": ["Sweaters", "Blankets", "Carpets", "Knitted fabrics"],
    },
    "Spandex": {
        "category": "Man-made • Synthetic",
        "source": "Segmented polyurethane polymer",
        "composition": "Polyurethane-based elastomer",
        "microstructure": "Hard and soft polymer segments form a structure that allows large reversible deformation.",
        "macrostructure": "Very fine elastic filament, usually blended with other fibers.",
        "properties": ["Very high stretch", "Excellent recovery", "Lightweight", "Good fit"],
        "uses": ["Sportswear", "Swimwear", "Stretch denim", "Activewear"],
    },
}

QUIZ = [
    ("Which fiber is mainly composed of cellulose?", ["Wool", "Cotton", "Silk", "Nylon"], "Cotton"),
    ("Which fiber is a natural protein fiber?", ["Flax", "Cotton", "Wool", "Jute"], "Wool"),
    ("Which fiber comes from a silkworm cocoon?", ["Silk", "Rayon", "Acrylic", "Polyester"], "Silk"),
    ("Which synthetic fiber is known for very high elasticity?", ["Spandex", "Jute", "Flax", "Cotton"], "Spandex"),
    ("Which fiber is regenerated cellulose?", ["Rayon", "Wool", "Nylon", "Silk"], "Rayon"),
]

def home():
    st.title("🧵 Textile Fiber Hub")
    st.write("A learning and revision web app for textile fiber science.")
    c1, c2, c3 = st.columns(3)
    c1.metric("Fibers", len(FIBERS))
    c2.metric("Natural", sum("Natural" in f["category"] for f in FIBERS.values()))
    c3.metric("Man-made", sum("Man-made" in f["category"] for f in FIBERS.values()))
    st.subheader("App Features")
    st.write("📚 Explore fibers • 🔍 Compare fibers • 📝 Take quizzes • 🎓 Review exam notes")

def library():
    st.title("📚 Fiber Library")
    search = st.text_input("Search fiber", placeholder="Example: cotton")
    names = [n for n in FIBERS if search.lower() in n.lower()] if search else list(FIBERS)
    if not names:
        st.warning("No fiber found.")
        return
    name = st.selectbox("Select a fiber", names)
    f = FIBERS[name]
    st.header(name)
    st.caption(f["category"])
    a, b = st.columns(2)
    with a:
        st.subheader("Source")
        st.write(f["source"])
        st.subheader("Composition")
        st.write(f["composition"])
        st.subheader("Microstructure")
        st.write(f["microstructure"])
    with b:
        st.subheader("Macrostructure")
        st.write(f["macrostructure"])
        st.subheader("Properties")
        for x in f["properties"]: st.write("• " + x)
        st.subheader("Uses")
        for x in f["uses"]: st.write("• " + x)

def compare():
    st.title("🔍 Compare Fibers")
    choices = st.multiselect("Choose 2–4 fibers", list(FIBERS), default=["Cotton", "Wool"])
    if len(choices) < 2:
        st.info("Select at least two fibers.")
        return
    rows = ["Category", "Source", "Composition", "Microstructure", "Macrostructure", "Properties", "Uses"]
    data = {}
    for name in choices:
        f = FIBERS[name]
        data[name] = [
            f["category"], f["source"], f["composition"], f["microstructure"],
            f["macrostructure"], ", ".join(f["properties"]), ", ".join(f["uses"])
        ]
    st.dataframe(pd.DataFrame(data, index=rows), use_container_width=True)

def quiz():
    st.title("📝 Fiber Quiz")
    with st.form("quiz"):
        answers = []
        for i, (q, options, correct) in enumerate(QUIZ):
            answers.append(st.radio(f"{i+1}. {q}", options, key=f"q{i}"))
        submit = st.form_submit_button("Check Score")
    if submit:
        score = sum(a == q[2] for a, q in zip(answers, QUIZ))
        st.success(f"Your score: {score}/{len(QUIZ)}")
        for i, (answer, item) in enumerate(zip(answers, QUIZ), 1):
            st.write(f"{'✅' if answer == item[2] else '❌'} Question {i}: {item[2]}")

def notes():
    st.title("🎓 Exam Notes")
    notes = {
        "What is a textile fiber?": "A textile fiber is a material with suitable length, fineness, strength, and flexibility for making yarns or textile products.",
        "What is microstructure?": "Microstructure describes microscopic organization such as polymer chains, crystalline regions, amorphous regions, and internal fiber layers.",
        "What is macrostructure?": "Macrostructure describes the larger physical form of a fiber, including length, diameter, surface, cross-section, and appearance.",
        "What is polymer crystallization?": "Polymer crystallization is the formation of more ordered regions when polymer chains arrange themselves during cooling from a melt or under suitable solution conditions.",
    }
    for q, a in notes.items():
        with st.expander(q): st.write(a)

st.sidebar.title("🧵 Textile Fiber Hub")
page = st.sidebar.radio("Navigation", ["Home", "Fiber Library", "Compare Fibers", "Quiz", "Exam Notes"])

if page == "Home": home()
elif page == "Fiber Library": library()
elif page == "Compare Fibers": compare()
elif page == "Quiz": quiz()
else: notes()
