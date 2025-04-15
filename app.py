import streamlit as st

# Set up page
st.set_page_config(layout="centered")

# Centered page title
st.markdown("<h1 style='text-align: center;'>2025 Los Angeles County Wildfire Timeline</h1>", unsafe_allow_html=True)

# Timeline entries
timeline_entries = [
    {
        "title": "Jan 7, 2025 – Multiple Fires Ignite",
        "image": "https://people.com/thmb/bqQbeNcHW-BZ6pfxr6w-OXz1djM=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc():focal(999x0:1001x2)/Pacific-Palisades-fire-010725-13-27011ac2a1e841b695cf3647d0202c13.jpg",
        "description": "Santa Ana winds and drought spark wildfires across LA County. The Palisades, Eaton, and Hurst fires force mass evacuations, including seniors and over 44,000 San Fernando Valley residents. Power outages, gridlock, and red flag warnings add to the chaos. Cal Fire, LAFD, Pasadena Fire, and the U.S. Forest Service lead emergency response."
    },
    {
        "title": "Jan 8, 2025 – Federal Disaster Declared",
        "image": "https://www.usatoday.com/gcdn/authoring/authoring-images/2025/01/09/USAT/77560462007-gty-2192342932.jpg?width=700&height=467&fit=crop&format=pjpg&auto=webp",
        "description": "Through the night, the Palisades and Eaton fires grow rapidly—reaching 3,000 and 1,000 acres by morning, both 0% contained. Winds hit 100 mph near the Eaton Fire. Two fatalities are confirmed, and Pasadena issues a do-not-drink water advisory. Hazardous air quality blankets the region. New fires erupt in the Sepulveda Basin, Acton, and the Hollywood Hills, prompting more evacuations. By evening, over 7,500 firefighters are deployed across LA County. Federal aid is approved, shelters open for both people and animals, and crews contain the Woodley Fire."
    },
    {
        "title": "Jan 9, 2025 – Fires Peak in Size",
        "image": "https://www.militarytimes.com/resizer/v2/S66E4CNBRRHMJOWVJBOMHSWUNU.jpg?auth=2cfb3b712bda2437c6478e6d5891ee8c0df1e5148ac8fc2d161a31c3534bc01c&width=8468&height=5645",
        "description": "The Palisades and Eaton fires grow to 17,000 and 10,000 acres with no containment. Over 200,000 residents have faced evacuation warnings or orders. The California National Guard is deployed, and President Biden announces full federal coverage of disaster response costs. New fires spark: the Kenneth Fire burns nearly 1,000 acres in West Hills, prompting evacuations, and a mistaken countywide alert causes widespread panic. The Sunset Fire in the Hollywood Hills is quickly contained. FEMA expands recovery efforts with aid centers in Altadena and West LA."
    },
    {
        "title": "Jan 10, 2025 – First Containment Lines Hold",
        "image": "https://ca-times.brightspotcdn.com/dims4/default/c866446/2147483647/strip/true/crop/6795x4655+0+0/resize/1200x822!/quality/75/?url=https%3A%2F%2Fcalifornia-times-brightspot.s3.amazonaws.com%2F77%2F1b%2F41d871b24b4f842c36a4b9ab5245%2F1476400-me-rpv-resident-living-without-power-jja-010.jpg",
        "description": "Containment begins—Palisades reaches 23,000 acres (6% contained) and Eaton 14,000 acres (1%). A countywide curfew is imposed to deter looting, and law enforcement teams with the National Guard to patrol fire-hit areas. The Archer Fire breaks out in Granada Hills but is swiftly contained. Governor Newsom orders an investigation into water system failures during the early stages of the Palisades Fire. Power restoration continues, though 18,000 remain without electricity. With calmer winds, crews strengthen fire lines. Air quality remains hazardous, with residents urged to limit exposure and wear N95 masks."
    },
    {
        "title": "Jan 11, 2025 – Cause Investigation Begins",
        "image": "https://media-cldnry.s-nbcnews.com/image/upload/rockcms/2025-01/250109-eaton-mb-0901-92e750.jpg",
        "description": "The Palisades Fire reaches 21,000 acres (11% contained) and the Eaton Fire 14,000 acres (15%). A joint investigation, led by the ATF, begins into the fires’ causes, with utility infrastructure under scrutiny. Governor Newsom doubles National Guard deployment, while over 15,000 personnel battle the flames. The Lidia and Archer fires are fully contained, and a flare-up in the Sepulveda Basin is halted. With containment improving, damage assessments begin. At least 24 are confirmed dead, dozens injured or missing. Relief efforts expand, shelters fill, and donations surpass $6 million to support evacuees and survivors."
    },
    {
        "title": "Jan 12–13, 2025 – Stabilization & Lawsuits",
        "image": "https://ca-times.brightspotcdn.com/dims4/default/8ed7d78/2147483647/strip/true/crop/6720x3528+0+476/resize/1200x630!/quality/75/?url=https%3A%2F%2Fcalifornia-times-brightspot.s3.amazonaws.com%2Fc2%2F6f%2Fa6b4e6c847878883eb13c6447518%2F1489879-me-0108-palisades-fire-gem-010.jpg",
        "description": "A break in the winds allows firefighters to improve containment. Palisades holds at 23,448 acres (14% contained), and Eaton grows to 14,117 acres (33%). Crews stop the Eaton Fire’s advance toward Mt. Wilson. The death toll rises to 25, with nearly 30 people still missing. Red Flag Warnings persist, and power remains shut off in fire zones. With the Kenneth Fire fully contained, resources shift back to the main fires. Lawsuits begin against SoCal Edison and LADWP for alleged negligence. The Hurst Fire is 97% contained, and a new blaze—the Auto Fire—is quickly contained near the Ventura County line."
    },
    {
        "title": "Jan 14–16, 2025 – Recovery Phase Begins",
        "image": "https://www.washingtonpost.com/wp-apps/imrs.php?src=https://arc-anglerfish-washpost-prod-washpost.s3.amazonaws.com/public/GKSGUKYPFIBTCTBFCNZO5BG73A_size-normalized.jpg&w=1440",
        "description": "Containment improves—Palisades at 22% and Eaton at 55%—despite a return of Santa Ana winds. The death toll rises to 27, with over 30 people still missing. Damage assessments confirm more than 12,000 structures destroyed countywide. Schools remain closed in hard-hit areas due to smoke, and power outages continue in high-risk zones. Firefighters from across the western U.S. reinforce lines in the mountains as search-and-rescue operations continue. Evacuation orders begin to ease in fringe zones like Malibu and Calabasas. Cleanup efforts begin, with agencies launching hazardous waste removal from burned homes in preparation for full recovery."
    },
    {
        "title": "Jan 17–31, 2025 – Containment Achieved",
        "image": "https://ca-times.brightspotcdn.com/dims4/default/e6db07a/2147483647/strip/false/crop/5280x2970+0+0/resize/1486x836!/quality/75/?url=https%3A%2F%2Fcalifornia-times-brightspot.s3.amazonaws.com%2F15%2F3f%2F7519e02f4e2897f0c7bc199f721c%2F1492330-me-0126-altadena-rain-rcg-550.jpg",
        "description": " Containment climbs steadily—Palisades at 100%, Eaton at 100% by month’s end. Light rain aids suppression but raises mudslide concerns. Over 200,000 were evacuated at the peak. As evacuation orders lift, residents return under curfews and checkpoints. FEMA opens more aid centers, and road crews work to reopen major routes. A new fire, the Hughes Fire near Castaic, burns 10,425 acres but is fully contained by January 30 with no structures lost. On January 31, Cal Fire declares the Palisades and Eaton Fires fully contained after 24 days. Governor Newsom pledges to expedite recovery as air quality improves across the region."
    },
    {
        "title": "Feb–Mar 2025 – Long-Term Recovery",
        "image": "https://s.yimg.com/ny/api/res/1.2/2voN.pM1iqsZ8XZbMzF9iQ--/YXBwaWQ9aGlnaGxhbmRlcjt3PTY0MDtoPTQzNA--/https://media.zenfs.com/en/la_times_articles_853/0128ece2471081cae9a254c9518c3d23",
        "description": "Recovery takes center stage. Over 170,000 residents apply for FEMA aid, and nonprofits shelter more than 20,000 evacuees. EPA completes record-fast hazardous waste cleanup across 1,600+ properties. Governor Newsom signs a $2.5 billion relief package to fund debris removal, rebuilding, and family assistance. By late March, federal aid tops $2 billion. The debris program expands to include commercial sites, and local crews work to stabilize hillsides and restore infrastructure. In total, 14 fires burned over 57,000 acres, destroying more than 18,000 structures. The Eaton and Palisades Fires caused 30 deaths and marked one of LA County’s most destructive wildfire disasters to date."
    }
]

# Session state for timeline position
if "index" not in st.session_state:
    st.session_state.index = 0

# Navigation functions
def go_previous():
    if st.session_state.index > 0:
        st.session_state.index -= 1

def go_next():
    if st.session_state.index < len(timeline_entries) - 1:
        st.session_state.index += 1

# Display current timeline entry
entry = timeline_entries[st.session_state.index]

st.markdown(f"<h3 style='text-align: center;'>{entry['title']}</h3>", unsafe_allow_html=True)
st.image(entry["image"], use_container_width=True)
st.markdown(f"<p style='text-align: center;'>{entry['description']}</p>", unsafe_allow_html=True)

# Navigation buttons
col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    if st.session_state.index > 0:
        st.button("⬅️ Previous", on_click=go_previous)
with col3:
    if st.session_state.index < len(timeline_entries) - 1:
        st.button("Next ➡️", on_click=go_next)

