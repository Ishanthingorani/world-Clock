import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo
import streamlit.components.v1 as components
from streamlit_autorefresh import st_autorefresh


# ----------------------------------
# PAGE CONFIG
# ----------------------------------

st.set_page_config(
    page_title="KYVEX GLOBAL - World Time Checker",
    page_icon="🌍",
    layout="wide"
    
    col_logo = st.columns(3)

with col_logo[1]:
    try:
 st.image(
    "FINAL_LOGO_2-removebg-preview.png",
    width=220
)
except:
    pass
)
st_autorefresh(
    interval=200,
    key="world_clock_refresh"
)


# ----------------------------------
# CUSTOM CSS
# ----------------------------------

st.markdown("""
<style>

.main {
    background-color:#f4f8fb;
}

.title{
    font-size:42px;
    font-weight:bold;
    color:#0B5394;
}

.subtitle{
    font-size:20px;
    color:#666666;
}

.bigtime{
    font-size:48px;
    color:#1E8E3E;
    font-weight:bold;
}

.card{
    background:white;
    padding:25px;
    border-radius:15px;
    box-shadow:0px 3px 10px rgba(0,0,0,.15);
}

.footer{
    text-align:center;
    color:gray;
    margin-top:40px;
}

</style>
""", unsafe_allow_html=True)


# ----------------------------------
# LOGO
# ----------------------------------




st.markdown(
    "<div class='title'>🌍 KYVEX GLOBAL</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>World Time Checker</div>",
    unsafe_allow_html=True
)


st.divider()


# ----------------------------------
# COUNTRY LIST
# ----------------------------------

countries = {

    "🇬🇧 United Kingdom":"Europe/London",

    "🇺🇸 United States":"America/New_York",

    "🇦🇺 Australia":"Australia/Sydney",

    "🇵🇭 Philippines":"Asia/Manila",

    "🇸🇬 Singapore":"Asia/Singapore",

    "🇬🇷 Greece":"Europe/Athens",

    "🇯🇵 Japan":"Asia/Tokyo",

    "🇸🇦 Saudi Arabia":"Asia/Riyadh",

    "🇺🇦 Ukraine":"Europe/Kyiv",

    "🇨🇳 China":"Asia/Shanghai"

}


# ----------------------------------
# SIDEBAR
# ----------------------------------

st.sidebar.header("Select Country")


selected = st.sidebar.selectbox(
    "Country",
    list(countries.keys())
)


timezone = countries[selected]


now = datetime.now(
    ZoneInfo(timezone)
)


hour = now.hour


if 9 <= hour < 18:
    status = "🟢 Business Hours"
else:
    status = "🔴 Outside Business Hours"



col1, col2 = st.columns([2,1])


# ==================================================
# LIVE CLOCK (AUTO SECOND COUNTING)
# ==================================================

with col1:

    st.markdown(
        "<div class='card'>",
        unsafe_allow_html=True
    )


    clock_html = f"""

    <html>

    <style>

    body {{
        margin:0;
        background:transparent;
        font-family:Arial;
    }}

    .clock {{
        text-align:center;
        font-size:48px;
        font-weight:bold;
        color:#0B5394;
    }}

    .date {{
        text-align:center;
        font-size:20px;
        color:#666;
        margin-top:10px;
    }}

    </style>


    <div class="clock" id="clock"></div>

    <div class="date" id="date"></div>



    <script>


    function updateClock() {{


        let current = new Date();


        let time = current.toLocaleTimeString(
            "en-US",
            {{
                timeZone:"{timezone}",
                hour:"2-digit",
                minute:"2-digit",
                second:"2-digit",
                hour12:true
            }}
        );


        let date = current.toLocaleDateString(
            "en-US",
            {{
                timeZone:"{timezone}",
                weekday:"long",
                year:"numeric",
                month:"long",
                day:"numeric"
            }}
        );


        document.getElementById("clock").innerHTML=time;

        document.getElementById("date").innerHTML=date;


    }}



    updateClock();


    setInterval(updateClock,1000);



    </script>


    """


    components.html(
        clock_html,
        height=120
    )


    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )
    
# ==================================================
# RIGHT SIDE PANEL
# ==================================================

with col2:

    st.markdown(
        "<div class='card'>",
        unsafe_allow_html=True
    )


    st.subheader("Business Hours")


    if 9 <= hour < 18:

        st.success("🟢 Office Open")

    else:

        st.error("🔴 Office Closed")


    st.write("")


    st.metric(
        label="Current Time",
        value=now.strftime("%I:%M:%S %p")
    )


    st.metric(
        label="Timezone",
        value=timezone
    )


    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )



st.write("")

st.divider()



# ==================================================
# ALL COUNTRIES LIVE DASHBOARD
# ==================================================

st.header("🌍 Live Time Across All Countries")


cards = st.columns(2)


index = 0


for country, tz in countries.items():


    current = datetime.now(
        ZoneInfo(tz)
    )


    if 9 <= current.hour < 18:

        business = "🟢 Open"

    else:

        business = "🔴 Closed"



    with cards[index % 2]:


        st.markdown(
            "<div class='card'>",
            unsafe_allow_html=True
        )


        st.subheader(country)


        st.markdown(
            f"""
            <div class='bigtime'>
            {current.strftime("%I:%M:%S %p")}
            </div>
            """,
            unsafe_allow_html=True
        )


        st.write(
            "📅",
            current.strftime("%A")
        )


        st.write(
            "🌐",
            tz
        )


        st.write(
            "Status:",
            business
        )


        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )


    index += 1



st.write("")

st.divider()



# ==================================================
# SEARCH COUNTRY
# ==================================================

st.header("🔍 Quick Country Search")


search = st.text_input(
    "Search Country",
    placeholder="Type USA, UK, Japan..."
)



if search:


    found = False


    for country, tz in countries.items():


        if search.lower() in country.lower():


            found = True


            t = datetime.now(
                ZoneInfo(tz)
            )


            st.success(
                f"Country Found : {country}"
            )


            c1,c2,c3 = st.columns(3)



            with c1:

                st.metric(
                    "Current Time",
                    t.strftime("%I:%M:%S %p")
                )


            with c2:

                st.metric(
                    "Date",
                    t.strftime("%d %b %Y")
                )


            with c3:

                if 9 <= t.hour < 18:

                    st.success("🟢 Open")

                else:

                    st.error("🔴 Closed")



    if not found:

        st.warning(
            "Country not found."
        )



st.divider()



# ==================================================
# LIVE TABLE
# ==================================================

st.header("📊 Live Country Dashboard")


table=[]


for country,tz in countries.items():


    current=datetime.now(
        ZoneInfo(tz)
    )


    if 9 <= current.hour < 18:

        status="🟢 Open"

    else:

        status="🔴 Closed"



    table.append({

        "Country":country,

        "Current Time":
        current.strftime("%I:%M:%S %p"),

        "Date":
        current.strftime("%d %b %Y"),

        "Timezone":tz,

        "Status":status

    })



st.dataframe(
    table,
    use_container_width=True,
    hide_index=True
)



st.divider()



# ==================================================
# SUMMARY
# ==================================================

open_count=0

closed_count=0



for tz in countries.values():


    t=datetime.now(
        ZoneInfo(tz)
    )


    if 9 <= t.hour < 18:

        open_count += 1

    else:

        closed_count += 1



c1,c2=st.columns(2)



with c1:

    st.metric(
        "🟢 Countries Open",
        open_count
    )



with c2:

    st.metric(
        "🔴 Countries Closed",
        closed_count
    )



st.divider()



# ==================================================
# WORLD CLOCKS
# ==================================================

st.header("🌎 World Clock")


clock_cols=st.columns(5)



for i,(country,tz) in enumerate(countries.items()):


    current=datetime.now(
        ZoneInfo(tz)
    )



    with clock_cols[i%5]:


        st.markdown(
        f"""

        <div style="
        background:white;
        border-radius:15px;
        padding:15px;
        margin-bottom:15px;
        box-shadow:0px 3px 10px rgba(0,0,0,.15);
        text-align:center;
        ">


        <h4>{country}</h4>


        <h2 style="color:#0B5394;">

        {current.strftime("%I:%M:%S %p")}

        </h2>


        </div>

        """,
        unsafe_allow_html=True
        )



st.divider()



# ==================================================
# CONTACT TIME RECOMMENDATION
# ==================================================

st.header("📞 Best Time to Contact")


recommendation=[]



for country,tz in countries.items():


    current=datetime.now(
        ZoneInfo(tz)
    )


    if 9 <= current.hour < 18:

        msg="✅ Best Time to Contact"


    elif 7 <= current.hour < 9:

        msg="🟡 Office Opening Soon"


    elif 18 <= current.hour < 20:

        msg="🟠 Office Closing Soon"


    else:

        msg="❌ Contact Later"



    recommendation.append({

        "Country":country,

        "Current Time":
        current.strftime("%I:%M:%S %p"),

        "Recommendation":msg

    })



st.dataframe(
    recommendation,
    hide_index=True,
    use_container_width=True
)



st.divider()



# ==================================================
# FOOTER
# ==================================================

st.markdown("""

<hr>

<div style="text-align:center;">

<h2 style="color:#0B5394;">
KYVEX GLOBAL
</h2>


<h4 style="color:gray;">
Committed to Better Health
</h4>


<p style="font-size:14px;color:gray;">

🌍 World Time Checker

<br>

Designed for International Business Communication

</p>


</div>

""",
unsafe_allow_html=True)
