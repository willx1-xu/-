# -*- coding: utf-8 -*-
"""
Apex Power Systems — static site generator
Regenerates all product / solution / support pages from the real
Alibaba International Station product materials (charging piles + controllers),
removing legacy power-distribution content and unifying nav/footer.
"""
import os, html

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = "https://www.link-jl.com"
EMAIL = "xuke@link-jl.com"
WHATSAPP = "https://wa.me/8613201571341"

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet">')

TOPBAR_LEFT = "EV Charging Infrastructure · Charging Piles · Intelligent Controllers"
TOPBAR_RIGHT = "Nanjing, Jiangsu, China · OEM/ODM · OCPP 1.6J / 2.0 Ready"

def head(title, desc, path, base):
    canon = SITE + "/" + path
    t = html.escape(title)
    d = html.escape(desc)
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{t}</title>
<meta name="description" content="{d}">
<link rel="canonical" href="{canon}">
<link rel="icon" href="{base}assets/apex-favicon.svg">
<meta property="og:type" content="website">
<meta property="og:title" content="{t}">
<meta property="og:description" content="{d}">
<meta property="og:url" content="{canon}">
<meta property="og:site_name" content="Apex Power Systems">
<meta name="twitter:card" content="summary_large_image">
{FONTS}
<link rel="stylesheet" href="{base}assets/site.css">
</head>
<body>'''

def topbar():
    return f'<div class="topbar"><div class="container"><span>{TOPBAR_LEFT}</span><span>{TOPBAR_RIGHT}</span></div></div>'

def header(base, active=None):
    items = [
        ("", "Home"),
        ("products/", "Products"),
        ("solutions/", "Solutions"),
        ("about/", "About"),
        ("quality/", "Quality"),
        ("contact/", "Contact"),
    ]
    links = "".join(
        f'<a href="{base}{p}"{" class=\"active\"" if active is not None and p.rstrip("/")==active else ""}>{label}</a>'
        for p, label in items
    )
    return (f'<header><div class="container nav"><a href="{base}" class="brand">'
            f'<span class="mark">A</span><span>Apex Power Systems</span></a>'
            f'<div class="navlinks">{links}</div>'
            f'<a class="btn btn-orange navbtn" href="{base}contact/">Request A Quote</a></div></header>')

def footer(base):
    return f'''<footer><div class="container"><div class="footer-grid">
<div><a href="{base}" class="brand foot-brand"><span class="mark">A</span><span>Apex Power Systems</span></a>
<p>EV charging piles and intelligent charging controllers from 7kW to 480kW, with OCPP 1.6J / 2.0 readiness for global charging infrastructure.</p>
<p>Email: <a href="mailto:{EMAIL}">{EMAIL}</a><br>WhatsApp: +86 13201571341</p></div>
<div><h4>Charging Piles</h4><ul>
<li><a href="{base}products/7kw-single-gun-ac-charging-pile/">7kW AC Charging Pile</a></li>
<li><a href="{base}products/40kw-single-gun-integrated-dc-charging-pile/">40kW DC Charging Pile</a></li>
<li><a href="{base}products/160kw-400kw-integrated-dc-dual-gun-charging-pile/">160kW DC Dual-Gun Pile</a></li>
<li><a href="{base}products/400kw-heavy-duty-truck-dc-charger/">400kW Truck Charger</a></li>
<li><a href="{base}products/480kw-fully-flexible-group-charging-pile/">480kW Group Charging</a></li>
</ul></div>
<div><h4>Controllers &amp; Boards</h4><ul>
<li><a href="{base}products/apex-jc-6512-industrial-ev-dc-charging-station-controller/">JC-6512 DC Controller</a></li>
<li><a href="{base}products/apex-jc-6513-intelligent-ev-charging-hub-controller/">JC-6513 Hub Controller</a></li>
<li><a href="{base}products/jc-6650-ac-ev-charging-station-controller/">JC-6650 AC Controller</a></li>
<li><a href="{base}products/apex-jc-6620-ocpp-protocol-conversion-board/">JC-6620 OCPP Board</a></li>
<li><a href="{base}products/jc-1301-chademo-protocol-converter-board/">JC-1301 CHAdeMO Board</a></li>
</ul></div>
<div><h4>Solutions</h4><ul>
<li><a href="{base}solutions/ev-charging-station-power-solution/">Charging Station Solution</a></li>
<li><a href="{base}solutions/commercial-building-ev-charging-solution/">Commercial Building Charging</a></li>
<li><a href="{base}solutions/oem-odm-charging-equipment-solution/">OEM / ODM Equipment</a></li>
</ul></div>
<div><h4>Company</h4><ul>
<li><a href="{base}about/">About Apex</a></li>
<li><a href="{base}quality/">Quality Control</a></li>
<li><a href="{base}certificates/">Certificates</a></li>
<li><a href="{base}resources/">Resources</a></li>
<li><a href="{base}contact/">Contact / RFQ</a></li>
</ul></div>
</div><div class="footer-row"><span>© 2026 Apex Power Systems Co., Ltd.</span><span>EV Charging · Controllers · Grid-to-EV Solutions</span></div></div></footer>'''

RFQ_PRODUCT_OPTIONS = [
    "7kW Single-Gun AC Charging Pile",
    "40kW Single-Gun Integrated DC Charging Pile",
    "160kW Integrated DC Dual-Gun Charging Pile",
    "400kW Heavy-Duty Truck DC Charger",
    "480kW Fully Flexible Group Charging Pile",
    "JC-6512 DC Charging Controller",
    "JC-6513 Charging Hub Controller",
    "JC-6650 AC Charging Controller",
    "JC-6620 OCPP Protocol Board",
    "JC-1301 CHAdeMO Converter Board",
    "Complete Charging Station Solution",
]

def rfq_form(selected=None, placeholder="Power Rating / Connector / Protocol"):
    opts = ""
    for o in RFQ_PRODUCT_OPTIONS:
        sel = " selected" if o == selected else ""
        opts += f'<option{sel}>{o}</option>'
    return f'''<form name="rfq" method="POST" data-netlify="true" netlify-honeypot="bot-field"><input type="hidden" name="form-name" value="rfq"><p hidden><label>Do not fill this out: <input name="bot-field"></label></p><div class="form-grid"><input type="text" name="name" autocomplete="name" placeholder="Name" required><input type="email" name="email" autocomplete="email" placeholder="Email" required><input type="tel" name="phone" autocomplete="tel" placeholder="Phone / WhatsApp" required><input type="text" name="company" autocomplete="organization" placeholder="Company" required><input type="text" name="country" autocomplete="country-name" placeholder="Country" required><select name="interest" class="full" required><option value="" selected disabled>Product Interest</option>{opts}</select><input type="text" name="voltage_capacity_power" autocomplete="off" placeholder="{placeholder}" required><input type="text" name="quantity_project_scale" autocomplete="off" placeholder="Quantity / Project Scale" required><textarea name="message" placeholder="Technical requirements or project description" required></textarea><button class="btn btn-orange full" type="submit">Submit RFQ</button></div></form>'''

def spec_table(rows):
    trs = "".join(f"<tr><td>{p}</td><td>{v}</td></tr>" for p, v in rows)
    return f'<table><tr><th>Parameter</th><th>Specification</th></tr>{trs}</table>'

def benefit_cards(benefits, cols=3):
    cards = "".join(f"<div class='card'><h3>{b[0]}</h3><p>{b[1]}</p></div>" for b in benefits)
    return f'<div class="grid grid-{cols}">{cards}</div>'

def apps(items):
    return '<div class="applications">' + "".join(f"<span>{x}</span>" for x in items) + "</div>"

def faq(items):
    out = ""
    for q, a in items:
        out += f"<details><summary>{q}</summary><p>{a}</p></details>"
    return f'<div class="faq">{out}</div>'

# ---------------------------------------------------------------------------
# Product data
# ---------------------------------------------------------------------------
PRODUCTS = [
dict(
 slug="7kw-single-gun-ac-charging-pile",
 name="7kW Single-Gun AC Charging Pile",
 tag="AC Charging",
 img="ac-charger.jpg",
 alt="7kW single-gun AC charging pile for commercial parking and workplace charging",
 desc="7kW single-gun AC charging pile with IEC 62196 Type 2 socket, OCPP 1.6J connectivity and RFID/APP authentication for residential, workplace, hotel and commercial parking charging.",
 hero="A 7kW single-gun AC charging pile with a Type 2 socket, smart authentication and OCPP-ready connectivity for residential, workplace, hotel and commercial parking deployments.",
 overview="The Apex 7kW single-gun AC charging pile is a compact wall-mounted or floor-standing AC charger for destination charging. Built around the Apex AC charging control platform, it delivers reliable 7kW AC charging with Type 2 compatibility, multi-mode user authentication and OCPP 1.6J cloud connectivity.",
 benefits=[
  ("Type 2 Compatibility", "IEC 62196 Type 2 socket with a 32A single-phase design for residential, workplace and commercial AC charging across IEC-aligned markets."),
  ("Multi-Mode Authentication", "RFID card, mobile APP and QR code access give property managers flexible control over who can charge and when."),
  ("OCPP-Ready Connectivity", "OCPP 1.6J support with WiFi / 4G / Ethernet options connects to mainstream charging platforms and private management systems."),
  ("Safe AC Charging", "On-board overcurrent, overvoltage and residual-current (leakage) protection safeguards vehicles, users and the building supply."),
  ("Compact Installation", "Slim wallbox footprint with floor-standing or wall-mounted options suits parking garages, hotels and office lots with short install times."),
  ("Dynamic Load Management", "Multiple units coordinate to balance building load and maximise the number of charging points within existing capacity."),
 ],
 specs=[
  ("Charging Standard", "IEC 62196 Type 2 (IEC 61851-1 aligned)"),
  ("Rated Power", "7kW (single-phase AC 230V)"),
  ("Max Current", "32A (single-phase)"),
  ("Output", "AC 230V, 50/60Hz"),
  ("Protocol", "OCPP 1.6J (cloud platform ready)"),
  ("Authentication", "RFID (ISO 14443) / APP / QR code"),
  ("Protection", "IP54 · overcurrent · overvoltage · residual current"),
  ("Operating Temperature", "-30°C to +55°C"),
 ],
 applications=["Residential communities", "Workplace parking", "Hotels & hospitality", "Commercial parking lots", "Destination charging", "Apartment & condo EVSE"],
 faq=[
  ("What vehicles can this 7kW AC pile charge?", "Any electric vehicle with a Type 2 (IEC 62196) inlet can charge at 7kW AC, covering most passenger EVs and plug-in hybrids in European and IEC-aligned markets."),
  ("Can multiple piles be installed in one building?", "Yes. Multiple units support dynamic load management to balance the building supply and maximise charging points without grid upgrades."),
  ("Can the pile be branded for a property or operator?", "Yes. Appearance, labelling and interface can be customised under OEM/ODM cooperation for branded or private-label deployment."),
 ],
),

dict(
 slug="40kw-single-gun-integrated-dc-charging-pile",
 name="40kW Single-Gun DC Charging Pile",
 tag="DC Charging",
 img="dc-40kw-charger.jpg",
 alt="40kW single-gun integrated DC fast charging pile",
 desc="40kW single-gun integrated DC fast charging pile with 200-1000V output, ≥96% efficiency, OCPP 1.6J and OTA remote upgrade for retail, fleet and destination charging.",
 hero="A 40kW single-gun integrated DC fast charger with ≥96% efficiency, 200–1000V output and OCPP-ready connectivity for retail, fleet and destination charging.",
 overview="The Apex 40kW single-gun DC charging pile is an integrated DC fast charger for commercial, fleet and destination charging sites. High-efficiency DC modules, millisecond-level protection and triple-network connectivity make it a reliable workhorse for mid-power DC charging deployments.",
 benefits=[
  ("≥96% Conversion Efficiency", "High-efficiency DC modules reduce operating electricity costs by 3–4% versus lower-efficiency products, shortening station payback."),
  ("Millisecond Safety Protection", "Over/under-voltage, overcurrent, short-circuit, leakage, over-temperature, over-charge and lightning protection respond at millisecond speed, coordinated with the vehicle BMS."),
  ("Intelligent Forced-Air Cooling", "Temperature-controlled fans adjust to module temperature for stable full-power output across -20°C to +50°C, even in humid or desert climates."),
  ("4G / WiFi / Ethernet + OTA", "OCPP 1.6J connectivity to mainstream charging platforms, with OTA remote firmware updates that eliminate on-site dispatch for fixes and features."),
  ("Compact All-in-One Design", "Small footprint with floor-standing or wall-mounted options for malls, hotels, offices, industrial parks, hospitals and taxi centres."),
  ("10+ Year Service Life", "Anti-corrosion, UV-resistant and salt-spray-treated housing with IP54 protection, built from reputable-brand core components and full-load tested."),
 ],
 specs=[
  ("Rated Power", "40kW"),
  ("Input Voltage", "AC 380V ±20%"),
  ("Output Voltage", "200V–1,000V DC"),
  ("Output Current", "0–120A (adjustable)"),
  ("Efficiency", "≥96%"),
  ("Control", "RFID / APP / Plug &amp; Play"),
  ("Protocol", "OCPP 1.6J · 4G / WiFi / Ethernet"),
  ("IP Rating", "IP54"),
  ("Operating Temperature", "-20°C to +50°C"),
  ("Standards", "Aligned with GB/T &amp; IEC"),
 ],
 applications=["Retail & commercial sites", "Fleet charging", "Destination charging", "Hotel & office parking", "Taxi operation centres", "Industrial parks"],
 faq=[
  ("What information is needed for a 40kW DC pile quotation?", "Project country, grid input voltage, connector type, quantity, installation environment and any OEM/ODM requirements."),
  ("Does the pile support remote management?", "Yes. OCPP 1.6J over 4G/WiFi/Ethernet connects to mainstream charging platforms, with OTA remote firmware upgrades."),
  ("Can the 40kW pile operate in hot climates?", "Yes. Intelligent forced-air cooling maintains full rated power across -20°C to +50°C without derating."),
 ],
),

dict(
 slug="160kw-400kw-integrated-dc-dual-gun-charging-pile",
 name="160kW Integrated DC Dual-Gun Charging Pile",
 tag="DC Charging",
 img="dc-40kw-charger.jpg",
 alt="160kW integrated DC dual-gun fast charging pile",
 desc="160kW integrated DC dual-gun charging pile with intelligent power sharing (single 160kW / dual 80kW+80kW), HD touchscreen, multi-payment and OCPP 1.6J for public fast charging.",
 hero="A 160kW integrated DC dual-gun fast charger with intelligent power sharing, HD touchscreen and multi-payment support for public and commercial fast charging.",
 overview="The Apex 160kW integrated DC dual-gun charging pile serves two vehicles from one unit with intelligent power distribution — full 160kW to a single vehicle or on-demand 80kW+80kW to two. It is built for public fast-charging sites, highway service areas and commercial operators.",
 benefits=[
  ("Dual-Gun Power Sharing", "One unit serves two vehicles; 160kW to a single car or 80kW+80kW dynamically split, maximising site and equipment utilisation."),
  ("80% Charge in 30 Minutes", "In single-gun 160kW mode, mainstream 60–100kWh passenger EVs reach 80% in ~30 minutes for highway service area fast-charging demand."),
  ("HD Touchscreen & Multi-Payment", "High-definition touchscreen with multi-language support plus RFID, APP QR, WeChat/Alipay and credit-card payment for global users."),
  ("Heavy-Duty Anti-Corrosion Build", "Steel frame with pickling, phosphating and electrostatic spraying, multi-layer sealing and IP54 protection for long outdoor service."),
  ("Fleet & Billing Integration", "Built-in time/energy/member billing and third-party fleet-platform integration for data statistics, cost management and fault alerts."),
  ("Full OEM Customisation", "RAL colour, logo printing, 3–10m cable length and OCPP 1.6J/2.0 protocol options for branded and export deployments."),
 ],
 specs=[
  ("Total Power", "160kW"),
  ("Power Distribution", "Single 160kW / Dual 80kW + 80kW"),
  ("Output Voltage", "200V–1,000V DC"),
  ("Max Current", "Single gun up to 250A"),
  ("Efficiency", "≥96%"),
  ("Display", "HD touchscreen"),
  ("Communication", "OCPP 1.6J · 4G · Ethernet"),
  ("IP Rating", "IP54"),
 ],
 applications=["Public charging stations", "Highway service areas", "Commercial parking", "Fleet charging", "Retail & destination sites", "Charging operator networks"],
 faq=[
  ("How does the dual-gun power distribution work?", "With one vehicle connected the full 160kW is available; with two vehicles, power is split on-demand up to 80kW each based on real-time charging demand."),
  ("What payment methods are supported?", "RFID card, APP QR code, WeChat/Alipay, credit card and other methods, compatible with mainstream operation platforms."),
  ("Can this pile be branded for an operator?", "Yes. RAL-standard colours, logo printing, cable length (3–10m) and protocol options are available under OEM customisation."),
 ],
),

dict(
 slug="400kw-heavy-duty-truck-dc-charger",
 name="400kW Heavy-Duty Truck DC Charger",
 tag="Fleet Charging",
 img="heavy-duty-charger.jpg",
 alt="400kW heavy-duty truck DC charger for port, mining and logistics fleets",
 desc="400kW heavy-duty truck DC charger with 300A single-gun output, reinforced cables, anti-vibration structure and BMS auto-recognition for port, mining and logistics fleet charging.",
 hero="A 400kW heavy-duty truck DC charger engineered for electric trucks and buses in port, mining and logistics operations, with reinforced structure and BMS auto-recognition.",
 overview="The Apex 400kW heavy-duty truck DC charger is purpose-built for high-power fleet charging of new-energy trucks and buses (200–600kWh batteries). Reinforced cables, anti-vibration structure and automatic BMS recognition deliver 30–40 minute replenishment in the toughest operating environments.",
 benefits=[
  ("400kW Ultra-High Power", "300A single-gun output across 200–1,000V (extendable to 1,500V) refuels a heavy truck in 30–40 minutes, cutting transport turnaround time."),
  ("Reinforced Charging Cables", "Thickened copper core with double shielding and embedded tensile steel wire resists wear, oil and aging in port, mine and depot environments."),
  ("Automatic Heavy-Truck BMS Recognition", "Identifies CATL, BYD, Guoxuan, EVE and other battery protocols to apply each brand's recommended charging strategy and protect battery health."),
  ("Port & Mining Reinforced Structure", "Anti-loosening nuts, elastic damping pads and independent vibration brackets for 9+ years of reliable service under severe vibration."),
  ("Lightning & Surge Protection", "IEC 62305-aligned lightning protection with HV/LV physical isolation and insulation panels for high-risk port and mining sites."),
  ("Fleet Platform Integration", "Deep integration with fleet management, port TOS and mining dispatch systems for task dispatch, statistics and automatic cost settlement."),
 ],
 specs=[
  ("Rated Power", "400kW"),
  ("Output Voltage", "200V–1,000V (extendable to 1,500V)"),
  ("Max Current", "Single gun up to 300A"),
  ("Power Split", "Single 400kW / Dual 200kW + 200kW"),
  ("Cable Type", "Reinforced copper core + tensile steel wire"),
  ("Noise", "≤65 dB"),
  ("IP Rating", "IP54"),
  ("Standards", "Aligned with GB/T &amp; IEC"),
 ],
 applications=["Port container terminals", "Mining operations", "Logistics depots", "Heavy-truck fleet centres", "Bus depots", "High-power freight hubs"],
 faq=[
  ("Which vehicles is the 400kW charger designed for?", "New-energy heavy-duty trucks and buses with 200–600kWh batteries, covering CATL, BYD, Guoxuan and EVE battery protocols."),
  ("How fast does it charge a heavy truck?", "A single truck can be replenished in roughly 30–40 minutes at 400kW, significantly reducing fleet turnaround time."),
  ("Can it withstand port and mining conditions?", "Yes. Anti-loosening fasteners, damping brackets, reinforced cables and surge protection target high-vibration, high-risk environments."),
 ],
),

dict(
 slug="480kw-fully-flexible-group-charging-pile",
 name="480kW Fully Flexible Group Charging Pile",
 tag="Group Charging",
 img="flexible-480kw.jpg",
 alt="480kW fully flexible group charging system serving multiple vehicles",
 desc="480kW fully flexible group charging system serving 6-8 vehicles with per-gun 40-480kW dynamic allocation, ≥97% efficiency, V2G option and OCPP 1.6J for high-traffic stations.",
 hero="A 480kW fully flexible group charging system that dynamically allocates power across 6–8 vehicles for high-traffic charging stations.",
 overview="The Apex 480kW fully flexible group charging system pools 480kW (extendable to 800kW) and allocates power to each gun in real time. It serves everything from 20kWh passenger EVs to 600kWh heavy trucks from one system, with module-level fault isolation and V2G readiness.",
 benefits=[
  ("Fully Flexible Power Pool", "Real-time power allocation to each gun responds to each vehicle's BMS demand — one system serves passenger cars to heavy trucks."),
  ("2–3× Space Turnover", "6–8 vehicles charge simultaneously, delivering 2–3× the daily sessions of fixed-power piles and shortening station payback."),
  ("95%+ Model Compatibility", "200–1,000V (extendable to 1,500V) and 0–400A per gun cover BYD, Tesla, Li Auto, NIO, Xpeng and over 95% of national-standard EVs."),
  ("Module-Level Fault Isolation", "Each power module has independent control and protection; a failed module is isolated and power redistributed for 99.5%+ availability."),
  ("Orderly Charging & Tariff Optimisation", "Dynamic scheduling with time-of-use tariffs can cut station electricity costs by 30%+, boosting operating profitability."),
  ("V2G & OTA Future-Proofing", "Optional V2G bidirectional charging and remote OTA upgrades open grid-service revenue and keep the system current."),
 ],
 specs=[
  ("Total Power", "480kW (customisable to 800kW)"),
  ("Simultaneous Vehicles", "6–8 vehicles"),
  ("Single Gun Range", "40kW–480kW (continuously adjustable)"),
  ("Output Voltage", "200V–1,000V (extendable to 1,500V)"),
  ("Single Gun Current", "0–400A (adjustable)"),
  ("Efficiency", "≥97%"),
  ("Power Factor", "≥0.99 (full load)"),
  ("Plug Life", "≥10,000 times"),
  ("IP Rating", "IP54 / IP55"),
  ("Standards", "CQC certified · aligned with GB/T &amp; IEC"),
 ],
 applications=["Expressway energy hubs", "Urban CBD parking", "Logistics parks", "Heavy-truck operation centres", "Ride-hailing & taxi hubs", "Port container energy stations"],
 faq=[
  ("How many vehicles can the 480kW system serve?", "It charges 6–8 vehicles simultaneously, scalable to 12 guns and 800kW for larger stations."),
  ("Does it work for both cars and trucks?", "Yes. Power is dynamically allocated from 40kW to 480kW per gun, covering compact EVs through 600kWh heavy trucks."),
  ("Can the system support V2G?", "Yes. Optional V2G bidirectional charging supports grid peak-shaving and frequency regulation, opening new revenue streams."),
 ],
),

dict(
 slug="apex-jc-6512-industrial-ev-dc-charging-station-controller",
 name="Apex JC-6512 Industrial EV DC Charging Controller",
 tag="DC Controller",
 img="jc6512-controller.jpg",
 alt="Apex JC-6512 industrial EV DC charging station controller",
 desc="Apex JC-6512 industrial EV DC charging controller with 12 output channels, 9 communication ports, OCPP 1.6/2.0 and multi-brand power module compatibility for 40-480kW stations.",
 hero="An industrial DC charging controller with 12 output channels, OCPP 1.6/2.0 and multi-brand power module compatibility for 40–480kW charging stations.",
 overview="The Apex JC-6512 (Simple Charge Series) is an industrial-grade DC charging controller and the control foundation for single-gun or dual-gun DC stations from 40kW to 480kW. Pre-integrated power-module protocols and payment/HMI support accelerate station development.",
 benefits=[
  ("Universal Power Module Compatibility", "Pre-integrated protocols for INFY, SINSXCEL, UU GREEN, HW, MEGMEET, Tonhe and WL eliminate custom driver development."),
  ("12 Channels & 9 Ports", "12 active output channels (12V/3A) and 9 CAN/RS485/RS232/Ethernet ports provide complete station control and monitoring."),
  ("OCPP 1.6 / 2.0 Dual Protocol", "Deploys under any major cloud charging platform or private system without firmware modification, protecting platform migrations."),
  ("Integrated Payment & HMI", "Local billing plus Nayax Vpos and Pax POS online payment, with DWIN-series HMI support for a complete commercial solution."),
  ("Industrial Reliability", "IEC 61000-4 EMC compliance, withstands DC bus ≥1000V, and operates from -25°C to +70°C for demanding outdoor deployment."),
  ("Standards-Ready Metering", "DL/T 645-compliant energy metering for accurate, integration-ready billing."),
 ],
 specs=[
  ("Model", "Apex JC-6512 (Simple Charge Series)"),
  ("Dimensions", "285 × 152 × 43 mm"),
  ("Supply Voltage", "DC 12V ±10%"),
  ("Digital Outputs", "12 active channels (12V/3A)"),
  ("Communication Ports", "9 (CAN, RS485, RS232, Ethernet)"),
  ("Protocol", "OCPP 1.6 / 2.0"),
  ("EMC Compliance", "IEC 61000-4 · withstands DC ≥1000V"),
  ("Energy Meter", "DL/T 645 compliant"),
  ("Payment", "Local billing · Nayax Vpos · Pax POS"),
  ("Power Modules", "INFY, SINSXCEL, UU GREEN, HW, MEGMEET, Tonhe, WL"),
  ("Operating Temperature", "-25°C to +70°C"),
 ],
 applications=["Commercial DC charging stations", "Fleet charging systems", "Community charging points", "Transport hub charging", "OEM charger manufacturing", "Station retrofits"],
 faq=[
  ("Which power modules does the JC-6512 support?", "INFY, SINSXCEL, UU GREEN, HW, MEGMEET, Tonhe and WL via pre-integrated protocols, plus custom protocols."),
  ("Does it support integrated payment?", "Yes. Local billing plus Nayax Vpos and Pax POS online payment terminals are supported natively."),
  ("What stations can it control?", "Single-gun or dual-gun DC charging stations from 40kW to 480kW."),
 ],
),

dict(
 slug="apex-jc-6513-intelligent-ev-charging-hub-controller",
 name="Apex JC-6513 Intelligent EV Charging Hub Controller",
 tag="Hub Controller",
 img="jc6513-controller.jpg",
 alt="Apex JC-6513 flagship intelligent EV charging hub controller",
 desc="Apex JC-6513 flagship EV charging hub controller with 50-channel neural-network dispatch, up to 1280kW system capacity, OCPP 2.0.1 and V2G/ISO 15118 readiness.",
 hero="The flagship Apex charging controller, managing up to 50 channels and 1280kW with neural-network power dispatch and V2G readiness.",
 overview="The Apex JC-6513 (Intelligent Dispatch Series) is the flagship of the Apex controller family, engineered for high-density power dispatch in large charging hubs. Its neural-network algorithm manages up to 50 channels and 1280kW of system power for next-generation ultra-fast charging infrastructure.",
 benefits=[
  ("Neural-Network Dispatch", "Manages up to 50 simultaneous channels and a 1280kW power envelope with real-time load balancing for large charging hubs."),
  ("Revenue-Maximising Allocation", "Continuously monitors grid load, vehicle state-of-charge and priority to eliminate static-allocation waste and prevent demand spikes."),
  ("OCPP 2.0.1 + V2G + ISO 15118", "Future-proof bidirectional energy flow enables grid services, demand response and energy arbitrage beyond OCPP 1.6-only controllers."),
  ("12-Port Communication Density", "Triple CAN, quad RS485, RS232, Ethernet and 4G/WiFi handle power modules, meters, payment, cloud and local networks without bottlenecks."),
  ("Full OEM / ODM Customisation", "Custom dispatch algorithms, cloud integration, enclosure design and white-label firmware with engineering support from SLD review to commissioning."),
  ("Industrial-Grade Build", "IEC 61000-4 EMC compliance and -25°C to +70°C operation for demanding outdoor and semi-outdoor installations."),
 ],
 specs=[
  ("Model", "Apex JC-6513 (Intelligent Dispatch Series)"),
  ("Dimensions", "320 × 180 × 50 mm"),
  ("Supply Voltage", "DC 12V ±10%"),
  ("Digital Outputs", "Up to 50 channels — neural-network dispatch"),
  ("System Power", "Up to 1280kW managed output"),
  ("Communication Ports", "12 (CAN ×3, RS485 ×4, RS232, Ethernet, 4G/WiFi)"),
  ("Protocol", "OCPP 2.0.1 · V2G / ISO 15118 ready"),
  ("Energy Meter", "DL/T 645 / MID compliant"),
  ("Payment", "Nayax, Pax POS, RFID, QR code, local billing"),
  ("Operating Temperature", "-25°C to +70°C"),
 ],
 applications=["Large EV charging hubs", "Highway rest stops", "Urban mobility hubs", "Commercial fleet charging", "Ultra-fast charging networks", "Charging station integrators"],
 faq=[
  ("What is the JC-6513's system capacity?", "It manages up to 50 charging channels and a total system power envelope of 1280kW."),
  ("Does it support V2G?", "Yes. OCPP 2.0.1 with V2G and ISO 15118 support enables bidirectional grid services and energy arbitrage."),
  ("Can the dispatch algorithm be customised?", "Yes. Custom dispatch algorithms, cloud integration, enclosure and white-label firmware are available under OEM/ODM."),
 ],
),

dict(
 slug="jc-6650-ac-ev-charging-station-controller",
 name="JC-6650 AC EV Charging Controller",
 tag="AC Controller",
 img="jc6650-controller.jpg",
 alt="JC-6650 AC EV charging station controller board",
 desc="JC-6650 AC charging controller with IEC 62196 Type 2, 7kW/11kW/22kW support, OCPP 1.6J/2.0.1, ISO 15118 Plug-and-Charge and MID metering for EU wallbox chargers.",
 hero="A European-standard AC charging controller supporting 7kW/11kW/22kW wallboxes with OCPP 1.6J/2.0.1, Plug-and-Charge and MID metering.",
 overview="The Apex JC-6650 is a professional AC charging controller designed for the European market, fully compliant with IEC 62196 Type 2. One hardware platform supports single-phase 7kW and three-phase 11kW/22kW configurations — the control core for smart residential, workplace and hospitality wallboxes.",
 benefits=[
  ("European Type 2 Compliance", "IEC 62196 Type 2 design for single-phase 7kW and three-phase 11kW/22kW wallbox chargers across IEC-aligned markets."),
  ("OCPP 1.6J / 2.0.1 + Plug-and-Charge", "ISO 15118 Plug-and-Charge enables seamless automatic vehicle authentication without RFID cards or app interaction."),
  ("MID-Certified Metering", "Built-in MID energy metering provides legally valid kWh billing for EU public and semi-public installations — no external meter needed."),
  ("Multi-Mode Authentication", "RFID (ISO 14443), APP, QR code, PIN and Plug-and-Charge on one hardware platform for fleet, public and premium residential use."),
  ("Dynamic Load Management", "Coordinates multiple units to maximise charging points within existing building capacity and prevent grid overload."),
  ("Outdoor-Ready Protection", "IP54 rating with integrated leakage-protection monitoring for reliable outdoor AC charging."),
 ],
 specs=[
  ("Model", "Apex JC-6650 (AC Smart Charging Controller)"),
  ("Charging Standard", "IEC 62196 Type 2 (IEC 61851-1 aligned)"),
  ("Supply Voltage", "AC 230V (1-phase) / AC 400V (3-phase)"),
  ("Power Range", "7kW (1-phase) / 11kW or 22kW (3-phase)"),
  ("Max Current", "16A / 32A"),
  ("Protocol", "OCPP 1.6J / 2.0.1 · ISO 15118 Plug-and-Charge"),
  ("Authentication", "RFID · APP · QR · PIN · Plug-and-Charge"),
  ("Metering", "MID-certified (EU billing compliant)"),
  ("Protection", "IP54 · integrated leakage monitoring"),
  ("Operating Temperature", "-30°C to +55°C"),
 ],
 applications=["Residential wallboxes", "Workplace charging", "Commercial car parks", "Hotel destination charging", "Fleet AC charging", "OEM wallbox manufacturing"],
 faq=[
  ("What power ratings does the JC-6650 support?", "Single-phase 7kW and three-phase 11kW/22kW from one hardware platform."),
  ("Is it compliant for EU billing?", "Yes. Built-in MID-certified metering enables legally valid kWh billing without external metering hardware."),
  ("Does it support Plug-and-Charge?", "Yes. ISO 15118 Plug-and-Charge provides automatic vehicle authentication for a seamless charging experience."),
 ],
),

dict(
 slug="apex-jc-6620-ocpp-protocol-conversion-board",
 name="Apex JC-6620 OCPP Protocol Board",
 tag="Protocol",
 img="ocpp-board.jpg",
 alt="Apex JC-6620 OCPP protocol conversion board",
 desc="Apex JC-6620 OCPP protocol conversion board with OCPP 1.6/2.0, Linux OS, dual Ethernet and EMC Grade A for European-standard EV charging cloud connectivity.",
 hero="An OCPP 1.6/2.0 protocol conversion board with Linux OS and dual Ethernet for European-standard charging cloud connectivity.",
 overview="The Apex JC-6620 is an OCPP protocol conversion board supporting OCPP 1.6 and OCPP 2.0 for European-standard EV charging infrastructure. Built on Linux with high-capacity storage, it delivers stable cloud connectivity and Grade A electromagnetic compatibility for industrial charging environments.",
 benefits=[
  ("OCPP 1.6 & 2.0 Support", "Full compatibility with European OCPP charging standards and cloud platforms."),
  ("Linux Operating System", "Large-capacity FLASH and RAM provide stable, long-term operation."),
  ("EMC Grade A", "High electromagnetic compatibility certified for industrial charging environments."),
  ("Dual Network Ports", "Dual Ethernet interfaces plus a USB download port for flexible connectivity."),
  ("Wide Input Voltage", "DC 9–36V input range for versatile power-supply compatibility."),
 ],
 specs=[
  ("Model", "Apex JC-6620 (OCPP Protocol Conversion Board)"),
  ("Dimensions", "165 × 120 × 45 mm"),
  ("Input Voltage", "DC 9–36V"),
  ("Protocol", "OCPP 1.6 / OCPP 2.0"),
  ("Operating System", "Linux"),
  ("Network Ports", "Dual Ethernet + USB download"),
  ("EMC", "Grade A"),
  ("Certification", "RoHS"),
 ],
 applications=["European charging networks", "OCPP cloud integration", "Charger protocol conversion", "Station retrofits", "OEM charging systems", "Networked charging platforms"],
 faq=[
  ("Which OCPP versions does the JC-6620 support?", "Both OCPP 1.6 and OCPP 2.0."),
  ("What operating system does it run?", "Linux, with large-capacity FLASH and RAM for stable long-term operation."),
  ("What connectivity does it provide?", "Dual Ethernet interfaces and a USB download port, with DC 9–36V wide input."),
 ],
),

dict(
 slug="jc-1301-chademo-protocol-converter-board",
 name="JC-1301 CHAdeMO Protocol Converter Board",
 tag="Protocol",
 img="chademo-board.jpg",
 alt="JC-1301 CHAdeMO protocol converter board",
 desc="JC-1301 CHAdeMO protocol converter board bridging CHAdeMO to GBT/CCS with CAN-bus isolation, surge protection and DIN-rail mounting for multi-standard DC charging.",
 hero="A CHAdeMO protocol converter that lets GBT/CCS DC stations serve Japanese-standard CHAdeMO vehicles without hardware redesign.",
 overview="The Apex JC-1301 is a dedicated CHAdeMO protocol conversion module that enables any GBT or CCS-based DC charging station to serve CHAdeMO-standard vehicles. Adding it to a station with a JC-6512 or JC-6513 controller immediately expands the serviceable vehicle base to Japanese-standard EVs.",
 benefits=[
  ("CHAdeMO-to-GBT/CCS Bridging", "Enables GBT/CCS DC stations to serve CHAdeMO vehicles without hardware redesign — plug-and-play with JC-6512/JC-6513."),
  ("Full Session Handshake", "Handles insulation detection, pre-charge, constant-current and termination phases for safe high-power DC charging sessions."),
  ("Industrial Shielding", "Aluminium and steel alloy enclosure provides superior EMI shielding versus PCB-only designs in high-amperage environments."),
  ("Dual-Voltage & DIN-Rail Mount", "DC 12V/24V compatible with DIN-rail or surface mounting for rapid installation in space-constrained cabinets."),
  ("Surge & Signal Isolation", "On-board surge protection and CAN-bus isolation prevent ground-loop interference and protect against connection transients."),
  ("Validated Vehicle Compatibility", "Tested with Nissan Leaf / e-NV200 / Ariya, Mitsubishi Outlander PHEV and other CHAdeMO brands."),
 ],
 specs=[
  ("Model", "Apex JC-1301 (CHAdeMO Protocol Conversion Module)"),
  ("Function", "Bi-directional bridge: CHAdeMO ↔ GBT / CCS"),
  ("Target Standard", "CHAdeMO (Japanese Standard)"),
  ("Operating Voltage", "DC 12V / 24V compatible"),
  ("Communication", "CAN bus (CHAdeMO primary)"),
  ("Mounting", "DIN rail or surface mount"),
  ("Protection", "Surge protection + CAN-bus signal isolation"),
  ("Enclosure", "Industrial-grade aluminium + steel alloy"),
  ("Operating Temperature", "-25°C to +70°C"),
 ],
 applications=["Multi-standard DC stations", "CHAdeMO vehicle markets", "Station retrofits", "OEM charging systems", "Mixed-fleet charging", "Japanese-standard compatibility"],
 faq=[
  ("What does the JC-1301 do?", "It converts between CHAdeMO and GBT/CCS so DC stations can serve Japanese-standard CHAdeMO vehicles."),
  ("Is it plug-and-play?", "Yes. It connects to a JC-6512 or JC-6513 main controller over the existing CAN bus with minimal configuration."),
  ("Which vehicles are compatible?", "Nissan Leaf / e-NV200 / Ariya, Mitsubishi Outlander PHEV and other CHAdeMO-adopting brands."),
 ],
),
]

# ---------------------------------------------------------------------------
# Solutions data
# ---------------------------------------------------------------------------
SOLUTIONS = [
dict(
 slug="ev-charging-station-power-solution",
 name="EV Charging Station Power Solution",
 img="flexible-480kw.jpg",
 alt="High-power EV charging equipment for a public charging station",
 desc="DC fast chargers, flexible group charging systems and OCPP-ready controllers for public, commercial and fleet charging station infrastructure.",
 hero="Charging piles, group charging systems and OCPP-ready controllers coordinated for public, commercial and fleet charging stations.",
 overview="The Apex EV Charging Station Power Solution combines AC/DC charging piles, flexible group charging systems and OCPP-ready controllers into a coordinated station architecture. It lets operators deploy public, commercial and fleet charging stations with one accountable equipment supplier.",
 architecture=[
  ("Power Supply", "Grid power is connected through project-based electrical design matched to station capacity."),
  ("Charging Piles", "AC and DC fast charging piles are selected according to station power and vehicle type."),
  ("Group Charging", "Flexible group charging systems pool and allocate power across multiple vehicles."),
  ("Intelligent Control", "OCPP-ready controllers manage charging sessions and station operation."),
  ("Network Integration", "OCPP 1.6J/2.0 connects the station to operator platforms and cloud management."),
 ],
 recommended=[
  ("ac-charger.jpg", "7kW Single-Gun AC Charging Pile", "AC destination charging for commercial and public sites."),
  ("dc-40kw-charger.jpg", "40kW Single-Gun DC Charging Pile", "Mid-power DC fast charging for retail and fleet sites."),
  ("flexible-480kw.jpg", "480kW Fully Flexible Group Charging Pile", "High-power pooled charging for high-traffic stations."),
  ("jc6513-controller.jpg", "JC-6513 Charging Hub Controller", "Intelligent OCPP-ready station control."),
 ],
 advantages=[
  ("Reduced Multi-Vendor Risk", "Charging piles, group systems and controllers are coordinated under one supplier architecture."),
  ("Project-Based Power Matching", "Equipment is selected according to charger power, number of points and site load demand."),
  ("OCPP-Ready Control", "Controllers support OCPP 1.6J / 2.0 for modern charging network integration."),
  ("OEM / ODM Support", "Pile appearance, controller interfaces and system configuration can be customised."),
 ],
 applications=["Public EV charging stations", "Commercial parking lots", "Fleet charging depots", "Heavy-duty truck charging", "Highway service areas", "Destination charging sites"],
 faq=[
  ("What equipment is needed for a charging station?", "Typically AC/DC charging piles, group charging systems, OCPP-ready controllers, cables, protection devices and monitoring."),
  ("Can Apex supply both piles and controllers?", "Yes. Apex provides AC/DC charging piles, group charging systems and intelligent charging controllers."),
  ("What information is needed for a station solution?", "Project country, grid voltage, planned charging power, number of chargers, vehicle type, site layout and communication requirements."),
 ],
),

dict(
 slug="commercial-building-ev-charging-solution",
 name="Commercial Building + EV Charging Solution",
 img="ac-charger.jpg",
 alt="AC EV charging equipment for commercial building parking",
 desc="AC/DC charging piles and intelligent controllers for hotels, offices, malls and commercial parking facilities.",
 hero="AC and DC charging piles with intelligent controllers for hotels, offices, malls and commercial parking facilities.",
 overview="The Apex Commercial Building + EV Charging Solution helps hotels, office buildings, shopping malls, parking facilities and mixed-use properties add reliable EV charging. It combines AC destination charging with DC fast charging and intelligent control for phased, expandable deployment.",
 architecture=[
  ("Building Power Supply", "Charging is supplied through the building's electrical infrastructure with load-managed coordination."),
  ("AC Charging Piles", "7kW AC piles provide destination charging for long-dwell parking."),
  ("DC Fast Charging", "DC piles serve shorter-stay users and high-turnover parking."),
  ("Load Management", "Controllers balance charging load within building capacity limits."),
  ("Smart Control", "OCPP-ready controllers support operation, billing and platform integration."),
 ],
 recommended=[
  ("ac-charger.jpg", "7kW Single-Gun AC Charging Pile", "AC destination charging for building parking."),
  ("dc-40kw-charger.jpg", "40kW Single-Gun DC Charging Pile", "DC fast charging for high-turnover parking."),
  ("jc6650-controller.jpg", "JC-6650 AC Charging Controller", "AC charging control and dynamic load management."),
 ],
 advantages=[
  ("Building-Friendly Equipment", "AC and DC charging pile options support indoor and commercial installation environments."),
  ("AC + DC Charging Options", "AC destination and DC fast charging combine according to parking duration and user needs."),
  ("Expandable Charging Layout", "Charging infrastructure can be planned for phased deployment and future expansion."),
  ("OEM / ODM Support", "Charging pile appearance, controller functions and configuration can be customised."),
 ],
 applications=["Office buildings", "Hotels", "Shopping malls", "Commercial parking lots", "Residential communities", "Destination charging sites"],
 faq=[
  ("Is charging suitable for commercial buildings?", "Yes. AC and DC charging piles support indoor commercial installation, with load management for existing supply."),
  ("Can Apex provide both AC and DC chargers?", "Yes. Apex provides 7kW AC charging piles plus multiple DC fast-charging options."),
  ("Can equipment be branded for a property?", "Yes. OEM/ODM options include appearance, interface, labelling and system integration."),
 ],
),

dict(
 slug="oem-odm-charging-equipment-solution",
 name="OEM / ODM Charging Equipment Solution",
 img="jc6513-controller.jpg",
 alt="OEM ODM charging controller and protocol board customization",
 desc="Charging controller, protocol board and charging pile customization for EV charger manufacturers and integration partners.",
 hero="Controller, protocol-board and charging-pile customisation for EV charger manufacturers and integration partners.",
 overview="The Apex OEM / ODM Charging Equipment Solution is built for charging pile manufacturers, station integrators, distributors and technology partners. It provides intelligent charging controllers, OCPP and CHAdeMO protocol boards, and product customisation to accelerate branded charger development.",
 architecture=[
  ("Product Definition", "Define charger type, charging power, standard, protocol, interface and target market."),
  ("Controller Selection", "Select JC-6512, JC-6513, JC-6650 or protocol boards according to the charger system."),
  ("Protocol Adaptation", "Support OCPP/CHAdeMO network communication and project-based integration."),
  ("OEM/ODM Customisation", "Appearance, interface, firmware logic and labelling can be customised."),
  ("Batch Support", "Support long-term partner development and product-series planning."),
 ],
 recommended=[
  ("jc6513-controller.jpg", "JC-6513 Charging Hub Controller", "Flagship DC hub control for OEM platforms."),
  ("jc6512-controller.jpg", "JC-6512 DC Charging Controller", "Industrial DC station control core."),
  ("jc6650-controller.jpg", "JC-6650 AC Charging Controller", "AC wallbox control board."),
  ("ocpp-board.jpg", "JC-6620 OCPP Protocol Board", "OCPP 1.6/2.0 cloud connectivity."),
 ],
 advantages=[
  ("Controller Portfolio", "AC, DC, hub and protocol-conversion controller options cover the full charger range."),
  ("OCPP Readiness", "Controllers are designed with OCPP 1.6J / 2.0 readiness for networked charging systems."),
  ("Protocol Conversion Support", "OCPP and CHAdeMO boards support market-specific charging integration requirements."),
  ("Private-Label Cooperation", "OEM/ODM supports appearance, interface, labelling and product development."),
 ],
 applications=["EV charger manufacturers", "Charging station integrators", "OEM charging brands", "Distributors", "Fleet charging equipment", "Protocol conversion projects"],
 faq=[
  ("Can Apex support charger OEM projects?", "Yes. Apex supports OEM/ODM charging equipment cooperation depending on product, specification and order requirements."),
  ("Which controller suits DC charging?", "JC-6512 and JC-6513 can be evaluated according to charger architecture and station requirements."),
  ("Can protocol boards be customised?", "Yes. Protocol and interface requirements can be discussed according to charger design and target market."),
 ],
),
]

# ---------------------------------------------------------------------------
# Render functions
# ---------------------------------------------------------------------------
def render_product(p):
    base = "../../"
    body = f'''{head(p['name']+" | Apex Power Systems", p['desc'], "products/"+p['slug']+"/", base)}
{topbar()}
{header(base)}
<main>
<section class="hero"><div class="container"><div><div class="crumb"><a href="../">Products</a> / {p['tag']}</div><span class="kicker">{p['tag']}</span><h1>{p['name']}</h1><p>{p['hero']}</p><a class="btn btn-orange" href="#rfq">Request Technical Datasheet</a><a class="btn btn-white" href="../">Back to Products</a></div><div class="hero-img"><img src="../../assets/{p['img']}" alt="{html.escape(p['alt'])}"></div></div></section>
<section><div class="container"><span class="kicker">Overview</span><h2>Product Overview</h2><p class="lead">{p['overview']}</p></div></section>
<section class="soft"><div class="container"><span class="kicker">Key Benefits</span><h2>Why Choose This Product</h2>{benefit_cards(p['benefits'])}</div></section>
<section><div class="container"><span class="kicker">Technical Parameters</span><h2>Specification Reference</h2><p class="lead">Final specifications can be customised according to project requirements.</p>{spec_table(p['specs'])}</div></section>
<section class="soft"><div class="container"><span class="kicker">Applications</span><h2>Typical Applications</h2>{apps(p['applications'])}</div></section>
<section><div class="container"><span class="kicker">FAQ</span><h2>Frequently Asked Questions</h2>{faq(p['faq'])}</div></section>
<section class="soft"><div class="container"><div class="rfq" id="rfq"><div><span class="kicker">Product RFQ</span><h2>Request Configuration for {p['name']}</h2><p>Send technical requirements, drawings, project country, charging power, protocol, quantity and customisation needs.</p></div>{rfq_form(selected=p['name'])}</div></div></section>
</main>
{footer(base)}
</body></html>'''
    write(os.path.join(ROOT, "products", p['slug'], "index.html"), body)

def render_solution(s):
    base = "../../"
    arch = "".join(f"<div class='card step'><b>{i+1}</b><h3>{a[0]}</h3><p>{a[1]}</p></div>" for i, a in enumerate(s['architecture']))
    recs = "".join(f"<div class='card product-card'><img src='../../assets/{r[0]}' alt='{r[1]}'><div class='body'><h3>{r[1]}</h3><p>{r[2]}</p></div></div>" for r in s['recommended'])
    body = f'''{head(s['name']+" | Apex Power Systems", s['desc'], "solutions/"+s['slug']+"/", base)}
{topbar()}
{header(base)}
<main>
<section class="hero"><div class="container"><div><div class="crumb"><a href="../">Solutions</a> / Charging</div><span class="kicker">Solution</span><h1>{s['name']}</h1><p>{s['hero']}</p><a class="btn btn-orange" href="#rfq">Discuss Your Project</a><a class="btn btn-white" href="../">Back to Solutions</a></div><div class="hero-img"><img src="../../assets/{s['img']}" alt="{html.escape(s['alt'])}"></div></div></section>
<section><div class="container"><span class="kicker">Overview</span><h2>Solution Overview</h2><p class="lead">{s['overview']}</p></div></section>
<section class="soft"><div class="container"><span class="kicker">System Architecture</span><h2>How the System Works</h2><div class="grid grid-5">{arch}</div></div></section>
<section><div class="container"><span class="kicker">Recommended Products</span><h2>Apex Products for This Solution</h2><div class="grid grid-4">{recs}</div></div></section>
<section class="soft"><div class="container"><span class="kicker">Advantages</span><h2>Why Choose Apex for This Solution</h2>{benefit_cards(s['advantages'], cols=2)}</div></section>
<section><div class="container"><span class="kicker">Applications</span><h2>Typical Applications</h2>{apps(s['applications'])}</div></section>
<section class="soft"><div class="container"><span class="kicker">FAQ</span><h2>Frequently Asked Questions</h2>{faq(s['faq'])}</div></section>
<section><div class="container"><div class="rfq" id="rfq"><div><span class="kicker">Solution RFQ</span><h2>Plan Your {s['name']}</h2><p>Send your project country, charging power, quantity, site layout and technical requirements. Apex will prepare a suitable solution configuration.</p></div><form name="rfq" method="POST" data-netlify="true" netlify-honeypot="bot-field"><input type="hidden" name="form-name" value="rfq"><p hidden><label>Do not fill this out: <input name="bot-field"></label></p><div class="form-grid"><input type="text" name="name" autocomplete="name" placeholder="Name" required><input type="email" name="email" autocomplete="email" placeholder="Email" required><input type="tel" name="phone" autocomplete="tel" placeholder="Phone / WhatsApp" required><input type="text" name="company" autocomplete="organization" placeholder="Company" required><input type="text" name="country" autocomplete="country-name" placeholder="Country" required><select name="interest" class="full" required><option value="" selected disabled>Solution Interest</option><option>EV Charging Station Power Solution</option><option>Commercial Building + EV Charging Solution</option><option>OEM / ODM Charging Equipment Solution</option></select><input type="text" name="voltage_capacity_power" autocomplete="off" placeholder="Charging Power / Connector / Protocol" required><input type="text" name="quantity_project_scale" autocomplete="off" placeholder="Project Scale / Quantity" required><textarea name="message" placeholder="Project requirements, drawings, or technical description" required></textarea><button class="btn btn-orange full" type="submit">Submit Solution RFQ</button></div></form></div></div></section>
</main>
{footer(base)}
</body></html>'''
    write(os.path.join(ROOT, "solutions", s['slug'], "index.html"), body)

def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", os.path.relpath(path, ROOT))

# ---------------------------------------------------------------------------
# Listing pages & support pages
# ---------------------------------------------------------------------------
PILE_CARDS = [
    ("ac-charger.jpg", "7kW Single-Gun AC Charging Pile", "Compact AC charging for commercial parking, hotels, workplace and residential projects.", "7kW · AC · Single Gun", "7kw-single-gun-ac-charging-pile/"),
    ("dc-40kw-charger.jpg", "40kW Single-Gun DC Charging Pile", "Integrated DC fast charging for retail, fleet and destination charging sites.", "40kW · DC · Single Gun", "40kw-single-gun-integrated-dc-charging-pile/"),
    ("dc-40kw-charger.jpg", "160kW Integrated DC Dual-Gun Charging Pile", "High-power integrated DC charging with intelligent dual-gun power sharing.", "160kW · DC · Dual Gun", "160kw-400kw-integrated-dc-dual-gun-charging-pile/"),
    ("heavy-duty-charger.jpg", "400kW Heavy-Duty Truck DC Charger", "High-power charging for electric trucks, buses and heavy-duty fleet depots.", "400kW · DC · Heavy Duty", "400kw-heavy-duty-truck-dc-charger/"),
    ("flexible-480kw.jpg", "480kW Fully Flexible Group Charging Pile", "Flexible power distribution across multiple guns for high-traffic stations.", "480kW · Group Charging", "480kw-fully-flexible-group-charging-pile/"),
]
CONTROLLER_CARDS = [
    ("jc6512-controller.jpg", "Apex JC-6512 DC Charging Station Controller", "Industrial controller for DC fast charging stations with OCPP network integration.", "DC Station Controller", "apex-jc-6512-industrial-ev-dc-charging-station-controller/"),
    ("jc6513-controller.jpg", "Apex JC-6513 Charging Hub Controller", "Intelligent hub controller for multi-gun stations and station management.", "Hub Controller", "apex-jc-6513-intelligent-ev-charging-hub-controller/"),
    ("jc6650-controller.jpg", "JC-6650 AC Charging Station Controller", "European-standard AC controller for 7kW/11kW/22kW smart wallboxes.", "AC Station Controller", "jc-6650-ac-ev-charging-station-controller/"),
]
BOARD_CARDS = [
    ("ocpp-board.jpg", "Apex JC-6620 OCPP Protocol Board", "OCPP 1.6/2.0 protocol conversion board for charging cloud connectivity.", "OCPP 1.6 / 2.0", "apex-jc-6620-ocpp-protocol-conversion-board/"),
    ("chademo-board.jpg", "JC-1301 CHAdeMO Converter Board", "Protocol converter board for CHAdeMO-compatible charging applications.", "CHAdeMO", "jc-1301-chademo-protocol-converter-board/"),
]

def _cards(cards, base):
    return "".join(
        f'''<article class="product-card">
<div class="image-box"><img src="{base}assets/{img}" alt="{name}"></div>
<div class="body"><h3>{name}</h3><p>{desc}</p>
<div class="actions"><span class="quote">{tag}</span><a class="link" href="{href}">View →</a></div></div>
</article>'''
        for img, name, desc, tag, href in cards
    )

def render_products_index():
    base = "../"
    piles = _cards(PILE_CARDS, base)
    ctrl = _cards(CONTROLLER_CARDS, base)
    boards = _cards(BOARD_CARDS, base)
    body = f'''{head("EV Charging Piles & Controllers | Apex Power Systems", "Browse Apex EV charging products: AC piles from 7kW, DC piles from 40kW to 480kW, and OCPP 1.6J/2.0-ready charging controllers and protocol boards.", "products/", base)}
{topbar()}
{header(base)}
<main>
<section class="hero"><div class="container"><div><span class="eyebrow">Apex Product Portfolio</span><h1>EV Charging Piles &amp; Controllers</h1><p>Two focused product families for global EV charging infrastructure: AC/DC charging piles from 7kW to 480kW, and OCPP 1.6J/2.0-ready charging station controllers and protocol conversion boards.</p><a class="btn btn-orange" href="#rfq">Send Product Requirements</a></div><div class="hero-img"><img src="../assets/flexible-480kw.jpg" alt="Apex EV charging equipment portfolio"></div></div></section>
<section class="soft"><div class="container">
<div class="product-nav"><a href="#charging-piles">Charging Piles</a><a href="#controllers">Controllers</a><a href="#protocol-boards">Protocol Boards</a></div>
<div class="category-section" id="charging-piles"><h2 class="category-title">AC &amp; DC Charging Piles</h2><p class="lead">From compact 7kW AC piles to 480kW flexible group charging systems for commercial, public, fleet and depot applications.</p><div class="product-grid" style="margin-top:28px">{piles}</div></div>
<div class="category-section" id="controllers"><h2 class="category-title">Charging Station Controllers</h2><p class="lead">Intelligent OCPP-ready controllers for AC and DC charging stations, hub operation and network integration.</p><div class="product-grid" style="margin-top:28px">{ctrl}</div></div>
<div class="category-section" id="protocol-boards"><h2 class="category-title">Protocol Conversion Boards</h2><p class="lead">Connect charging hardware to OCPP-based networks and legacy protocols.</p><div class="product-grid" style="margin-top:28px">{boards}</div></div>
</div></section>
<section class="soft"><div class="container"><div class="rfq" id="rfq"><div><span class="kicker">Product RFQ</span><h2>Request Charging Equipment Configuration</h2><p>Send your power rating, connector type, protocol, quantity, project country and customisation needs.</p></div>{rfq_form()}</div></div></section>
</main>
{footer(base)}
</body></html>'''
    write(os.path.join(ROOT, "products", "index.html"), body)

def render_solutions_index():
    base = "../"
    body = f'''{head("Charging Solutions | Apex Power Systems", "Apex charging solutions for EV charging stations, commercial buildings, fleet and high-power charging, and OEM/ODM charging equipment programs.", "solutions/", base)}
{topbar()}
{header(base)}
<main>
<section class="hero"><div class="container"><div><span class="kicker">Application Solutions</span><h1>EV Charging Solutions for Global Projects</h1><p>Apex helps charging station operators, EPC contractors, distributors and OEM partners deploy reliable EV charging infrastructure with charging piles and intelligent controllers.</p><a class="btn btn-orange" href="#solutions">Explore Solutions</a></div><div class="hero-img"><img src="../assets/flexible-480kw.jpg" alt="High-power EV charging equipment for global projects"></div></div></section>
<section id="solutions" class="soft"><div class="container"><div class="section-head"><div class="copy"><span class="kicker">Solution Portfolio</span><h2>Charging Solutions Built for Deployment</h2><p>Focused charging solutions covering station deployment, commercial buildings, fleet charging and OEM/ODM equipment programs.</p></div></div><div class="grid grid-2">
<article class="card solution-card"><img src="../assets/flexible-480kw.jpg" alt="EV charging station solution"><div class="body"><span class="kicker">Station</span><h3>EV Charging Station Solution</h3><p>Charging piles and OCPP-ready controllers for public, commercial and fleet charging station deployment.</p><a class="btn btn-orange" href="ev-charging-station-power-solution/">View Solution</a></div></article>
<article class="card solution-card"><img src="../assets/ac-charger.jpg" alt="Commercial building EV charging solution"><div class="body"><span class="kicker">Buildings</span><h3>Commercial Building Charging</h3><p>AC/DC charging for offices, hotels, malls and parking facilities.</p><a class="btn btn-white" href="commercial-building-ev-charging-solution/">View Solution</a></div></article>
<article class="card solution-card"><img src="../assets/jc6513-controller.jpg" alt="OEM ODM charging equipment solution"><div class="body"><span class="kicker">OEM / ODM</span><h3>OEM / ODM Charging Equipment</h3><p>Controller boards, protocol conversion, pile customisation and private label.</p><a class="btn btn-white" href="oem-odm-charging-equipment-solution/">View Solution</a></div></article>
</div></div></section>
<section class="soft"><div class="container"><div class="rfq" id="rfq"><div><span class="kicker">Project RFQ</span><h2>Discuss Your Charging Project</h2><p>Share your project type, power requirements, protocol, quantity and location.</p></div><form name="rfq" method="POST" data-netlify="true" netlify-honeypot="bot-field"><input type="hidden" name="form-name" value="rfq"><p hidden><label>Do not fill this out: <input name="bot-field"></label></p><div class="form-grid"><input type="text" name="name" autocomplete="name" placeholder="Name" required><input type="email" name="email" autocomplete="email" placeholder="Email" required><input type="tel" name="phone" autocomplete="tel" placeholder="Phone / WhatsApp" required><input type="text" name="company" autocomplete="organization" placeholder="Company" required><input type="text" name="country" autocomplete="country-name" placeholder="Country" required><select name="interest" class="full" required><option value="" selected disabled>Project Interest</option><option>EV Charging Station</option><option>Commercial Building Charging</option><option>Fleet / High-Power Charging</option><option>OEM / ODM Charging Equipment</option></select><input type="text" name="voltage_capacity_power" autocomplete="off" placeholder="Power Rating / Connector / Protocol" required><input type="text" name="quantity_project_scale" autocomplete="off" placeholder="Quantity / Project Scale" required><textarea name="message" placeholder="Project requirements or technical description" required></textarea><button class="btn btn-orange full" type="submit">Submit RFQ</button></div></form></div></div></section>
</main>
{footer(base)}
</body></html>'''
    write(os.path.join(ROOT, "solutions", "index.html"), body)

def render_ev_chargers_controllers():
    base = "../../"
    body = f'''{head("EV Chargers and EV Charger Controllers | Apex Power Systems", "Explore Apex AC/DC EV chargers, high-power charging equipment and OCPP-ready EV charger controllers for charging stations and OEM integration.", "products/ev-chargers-controllers/", base)}
{topbar()}
{header(base)}
<main>
<section class="hero"><div class="container">
<div><div class="crumb"><a href="../">Products</a> / EV Chargers &amp; Controllers</div><span class="kicker">EV Charger &amp; Controller</span><h1>Charging Equipment and Intelligent Control</h1><p>Apex provides AC/DC charging equipment, high-power group charging, station controllers and protocol conversion boards for charging operators, integrators and OEM partners.</p><div class="actions"><a class="btn btn-orange" href="#quote">Request a Quote</a><a class="btn btn-outline" href="#parameters">Technical Parameters</a></div></div>
<div class="hero-media"><img src="../../assets/flexible-480kw.jpg" alt="Apex high-power EV charging station equipment"></div>
</div></section>
<section><div class="container two-col"><div><span class="kicker">Overview</span><h2>From Charger Hardware to Station Control</h2><p class="lead">Select charging equipment by charging power and operating scenario, then coordinate controller and communication requirements for networked station deployment or OEM integration.</p></div><div><span class="kicker">Applications</span><div class="pills"><span>Public charging hubs</span><span>Fleet depots</span><span>Highway service areas</span><span>Commercial parking</span><span>OEM charger integration</span></div></div></div></section>
<section class="soft"><div class="container"><span class="kicker">Key Advantages</span><h2>Equipment and Control in One Portfolio</h2><div class="grid"><article class="card"><h3>AC and DC Charging</h3><p>Options span AC charging, integrated DC equipment and high-power flexible charging applications.</p></article><article class="card"><h3>Controller Support</h3><p>Station and charger controllers support integration requirements, including OCPP-ready solutions.</p></article><article class="card"><h3>OEM / ODM Cooperation</h3><p>Discuss equipment configuration, controller interface, protocol conversion and branding needs.</p></article></div></div></section>
<section id="parameters"><div class="container"><span class="kicker">Technical Parameters</span><h2>Quotation Inputs</h2><p class="lead">Charging and controller specifications are confirmed for the selected model and target market.</p><table><thead><tr><th>Parameter</th><th>Configuration Basis</th></tr></thead><tbody><tr><td>Equipment scope</td><td>AC charger, DC fast charger, flexible group charger, controller or protocol board</td></tr><tr><td>Power rating</td><td>Charging scenario, vehicle mix and site power allocation</td></tr><tr><td>Connector requirement</td><td>Destination market and intended vehicle compatibility</td></tr><tr><td>Communication / protocol</td><td>Platform connection and OEM integration requirement, including OCPP inquiry</td></tr><tr><td>Installation and enclosure</td><td>Indoor/outdoor placement, layout and operating environment</td></tr><tr><td>Customisation</td><td>Interface, labelling, configuration and documentation by confirmed requirement</td></tr></tbody></table></div></section>
<section class="soft"><div class="container"><span class="kicker">Product Image Area</span><h2>Charging and Control Products</h2><div class="product-area"><article class="product-card"><img src="../../assets/flexible-480kw.jpg" alt="480kW fully flexible group charging equipment"><div><h3>480kW Flexible Charging</h3><p>High-power charging deployment option.</p><a class="text-link" href="../480kw-fully-flexible-group-charging-pile/">View product &rarr;</a></div></article><article class="product-card"><img src="../../assets/dc-40kw-charger.jpg" alt="40kW integrated DC EV charger"><div><h3>DC Charging Equipment</h3><p>Integrated fast charger option.</p><a class="text-link" href="../40kw-single-gun-integrated-dc-charging-pile/">View product &rarr;</a></div></article><article class="product-card"><img src="../../assets/jc6513-controller.jpg" alt="Apex JC-6513 intelligent EV charging hub controller"><div><h3>Charging Controllers</h3><p>Intelligent station control and integration.</p><a class="text-link" href="../apex-jc-6513-intelligent-ev-charging-hub-controller/">View product &rarr;</a></div></article></div></div></section>
<section id="quote"><div class="container"><div class="contact-box"><div><span class="kicker">Request a Quote</span><h2>Discuss Your EV Charging Requirement</h2><p>Provide charging power, connector, protocol, quantity, installation scenario, destination market and controller or OEM needs.</p><div class="contact-links"><a href="mailto:{EMAIL}">{EMAIL}</a><a href="{WHATSAPP}">WhatsApp: +86 13201571341</a></div></div><a class="btn btn-orange" href="../../contact/">Open RFQ Form</a></div></div></section>
</main>
{footer(base)}
</body></html>'''
    write(os.path.join(ROOT, "products", "ev-chargers-controllers", "index.html"), body)

def render_about():
    base = "../"
    body = f'''{head("About Apex Power Systems", "Apex Power Systems Co., Ltd. is a China-based manufacturer specializing in EV charging piles and intelligent charging controllers, headquartered in Nanjing, Jiangsu, China.", "about/", base)}
{topbar()}
{header(base)}
<main>
<section class="hero"><div class="container"><div><span class="kicker">About Apex Power Systems</span><h1>EV Charging Piles &amp; Intelligent Controllers</h1><p>Apex Power Systems Co., Ltd. is a China-based manufacturer specializing in EV charging infrastructure, headquartered in Nanjing, Jiangsu, China.</p><a class="btn btn-orange" href="../contact/">Contact Apex</a></div><div class="hero-img"><img src="../assets/integrated/production-02.jpg" alt="About Apex Power Systems"></div></div></section>
<section><div class="container"><span class="kicker">Company Profile</span><h2>Charging Infrastructure for Global Projects</h2><p class="lead">Apex provides end-to-end EV charging solutions spanning AC/DC charging piles, group charging systems and intelligent charging station controllers with OCPP 1.6J / 2.0 readiness. Our portfolio covers AC piles from 7kW, DC fast charging from 40kW to 480kW, and a family of charging controllers and protocol conversion boards for station and network integration.</p><p class="lead">By combining charging equipment and intelligent control into a unified architecture, Apex helps customers reduce multi-vendor coordination risks and build more reliable charging infrastructure.</p></div></section>
<section class="soft"><div class="container"><span class="kicker">What We Provide</span><h2>Product &amp; Solution Capabilities</h2><div class="grid grid-3"><div class="card"><img src="../assets/flexible-480kw.jpg" alt="EV charging piles"><h3>EV Charging Piles</h3><p>AC/DC charging piles and high-power group charging systems for public, commercial and fleet charging projects.</p></div><div class="card"><img src="../assets/jc6513-controller.jpg" alt="Charging controllers"><h3>Intelligent Charging Controllers</h3><p>Charging station controllers and protocol boards for OEM, ODM and networked charging integration.</p></div><div class="card"><img src="../assets/ac-charger.jpg" alt="AC charging piles"><h3>AC &amp; DC Charging</h3><p>AC and DC charging equipment from 7kW to 480kW for commercial, public and fleet charging projects.</p></div></div></div></section>
<section><div class="container"><span class="kicker">Global Markets</span><h2>Serving Overseas Charging Projects</h2><p class="lead">Apex supports customers in North America, Europe, Southeast Asia, the Middle East and South America with OEM/ODM cooperation, IEC-compliant product design, technical documentation, project configuration and export-oriented communication.</p><div class="applications"><span>North America</span><span>Europe</span><span>Southeast Asia</span><span>Middle East</span><span>South America</span><span>OEM / ODM Partners</span></div></div></section>
</main>
{footer(base)}
</body></html>'''
    write(os.path.join(ROOT, "about", "index.html"), body)

def render_quality():
    base = "../"
    body = f'''{head("Quality & Manufacturing | Apex Power Systems", "Apex Power Systems manufacturing, testing, quality control and export delivery capability for EV charging piles and charging controllers.", "quality/", base)}
{topbar()}
{header(base)}
<main>
<section class="hero"><div class="container"><div><span class="kicker">Quality &amp; Manufacturing</span><h1>Manufacturing Capability for Charging Equipment</h1><p>Production, assembly, testing, inspection and export support for Apex EV charging piles and charging controllers.</p><a class="btn btn-orange" href="../contact/">Request Factory Information</a></div><div class="hero-img"><img src="../assets/integrated/production-01.jpg" alt="Apex manufacturing"></div></div></section>
<section><div class="container"><span class="kicker">Capability</span><h2>Production &amp; Inspection Process</h2><p class="lead">Apex supports project-based equipment supply through structured production coordination, assembly, inspection, testing, packing and technical documentation.</p><div class="grid grid-4"><div class="card step"><b>1</b><h3>Material Preparation</h3><p>Charging modules, controllers, enclosures, terminals and accessories are prepared according to order requirements.</p></div><div class="card step"><b>2</b><h3>Assembly</h3><p>Charging piles and controllers are assembled according to electrical design, layout, wiring requirements and project configuration.</p></div><div class="card step"><b>3</b><h3>Testing</h3><p>Routine tests and functional checks are performed according to product type and project needs.</p></div><div class="card step"><b>4</b><h3>Export Delivery</h3><p>Packing, documentation and delivery communication support overseas project requirements.</p></div></div></div></section>
<section class="soft"><div class="container"><span class="kicker">Factory Gallery</span><h2>Production Photos</h2><p class="lead">Real production and workshop materials help strengthen buyer confidence and project evaluation.</p><div class="grid grid-4"><div class='card'><img src='../assets/integrated/production-01.jpg' alt='Apex production 1'><span class='tag'>Manufacturing</span><h3>Production Workshop</h3><p>Workshop and equipment scenes supporting charging equipment manufacturing.</p></div><div class='card'><img src='../assets/integrated/production-02.jpg' alt='Apex production 2'><span class='tag'>Manufacturing</span><h3>Assembly Process</h3><p>Assembly process for EV charging piles and controllers.</p></div><div class='card'><img src='../assets/integrated/production-03.jpg' alt='Apex production 3'><span class='tag'>Manufacturing</span><h3>Testing &amp; Inspection</h3><p>Inspection and test processes supporting project delivery.</p></div><div class='card'><img src='../assets/integrated/production-04.jpg' alt='Apex production 4'><span class='tag'>Manufacturing</span><h3>Charging Equipment Production</h3><p>Production capability for charging piles, controllers and control equipment.</p></div><div class='card'><img src='../assets/integrated/production-05.jpg' alt='Apex production 5'><span class='tag'>Manufacturing</span><h3>Component Processing</h3><p>Production process and component preparation for customised equipment.</p></div><div class='card'><img src='../assets/integrated/production-11.jpg' alt='Automated fabrication equipment in the production workshop'><span class='tag'>Manufacturing</span><h3>Automated Fabrication</h3><p>Workshop production equipment supporting enclosure preparation.</p></div><div class='card'><img src='../assets/integrated/production-07.jpg' alt='Apex production 7'><span class='tag'>Manufacturing</span><h3>Workshop Management</h3><p>Manufacturing organisation supporting international project delivery.</p></div><div class='card'><img src='../assets/integrated/production-08.jpg' alt='Apex production 8'><span class='tag'>Manufacturing</span><h3>Quality Inspection</h3><p>Quality control and inspection supporting charging equipment supply.</p></div></div></div></section>
<section><div class="container"><span class="kicker">Quality Control</span><h2>Project-Based Quality Support</h2><div class="grid grid-3"><div class="card"><h3>Technical Review</h3><p>Review drawings, charging power, standard, connector, protocol and installation environment before production.</p></div><div class="card"><h3>Process Inspection</h3><p>Follow assembly inspection, wiring check, structure inspection and electrical test requirements.</p></div><div class="card"><h3>Documentation</h3><p>Provide datasheets, certificates, photos, packing information and export documents according to order needs.</p></div></div></div></section>
</main>
{footer(base)}
</body></html>'''
    write(os.path.join(ROOT, "quality", "index.html"), body)

def render_contact():
    base = "../"
    body = f'''{head("Contact Apex Power Systems | RFQ", "Contact Apex Power Systems at xuke@link-jl.com or WhatsApp +86 13201571341 for charging piles, charging controllers and charging equipment.", "contact/", base)}
{topbar()}
{header(base)}
<main>
<section class="hero"><div class="container"><div><span class="kicker">Contact / RFQ</span><h1>Request A Quote or Technical Proposal</h1><p>Send your charging power, connector type, protocol, project country, quantity and customisation requirements. Apex will help prepare a suitable product or solution recommendation.</p><a class="btn btn-orange" href="mailto:{EMAIL}">Email Apex</a><a class="btn btn-white" href="{WHATSAPP}">WhatsApp Apex</a></div><div class="hero-img"><img src="../assets/flexible-480kw.jpg" alt="EV charging infrastructure project supported by Apex"></div></div></section>
<section><div class="container"><div class="grid grid-3"><div class="card"><h3>Headquarters</h3><p>Nanjing, Jiangsu, China</p></div><div class="card"><h3>Email</h3><p><a href="mailto:{EMAIL}">{EMAIL}</a></p></div><div class="card"><h3>Phone / WhatsApp</h3><p><a href="tel:+8613201571341">+86 13201571341</a><br><a href="{WHATSAPP}">Open WhatsApp chat</a></p></div></div></div></section>
<section class="soft"><div class="container"><div class="rfq" id="rfq"><div><span class="kicker">RFQ Form</span><h2>Tell Us Your Project Requirements</h2><p>For charging piles, please provide charging power, connector type and quantity. For controllers and protocol boards, provide power rating, protocol, quantity and customisation requirements.</p></div>{rfq_form()}</div></div></section>
</main>
{footer(base)}
</body></html>'''
    write(os.path.join(ROOT, "contact", "index.html"), body)

def render_projects():
    base = "../"
    body = f'''{head("Applications & Delivery Support | Apex Power Systems", "Review Apex charging equipment application scenarios and delivery support for EV charging station, commercial and fleet projects.", "projects/", base)}
{topbar()}
{header(base)}
<main>
<section class="hero"><div class="container"><div><span class="kicker">Applications &amp; Delivery</span><h1>Equipment Support for Charging Projects</h1><p>Explore typical application scenarios and manufacturing support for Apex EV charging piles and charging controllers.</p><a class="btn btn-orange" href="../contact/">Discuss Your Project</a></div><div class="hero-img"><img src="../assets/integrated/production-03.jpg" alt="Charging equipment assembly capability supporting project supply"></div></div></section>
<section><div class="container"><span class="kicker">Applications</span><h2>Equipment Configuration Scenarios</h2><p class="lead">These examples describe equipment applications, not published customer case studies. Request relevant reference materials for a qualified procurement discussion.</p><div class="grid grid-2"><div class='card'><img src='../assets/flexible-480kw.jpg' alt='High-power EV charging equipment for charging station applications'><span class='tag'>Application</span><h3>EV Charging Infrastructure</h3><p>Integrated charging station infrastructure with AC/DC charging piles, group charging systems and intelligent controllers.</p></div><div class='card'><img src='../assets/integrated/production-11.jpg' alt='Charging equipment manufacturing workshop'><span class='tag'>Capability</span><h3>Manufacturing &amp; Delivery Support</h3><p>Production, assembly, inspection and delivery capability supporting overseas project supply.</p></div></div></div></section>
<section class="soft"><div class="container"><span class="kicker">How Apex Supports Projects</span><h2>From Requirements to Delivery</h2><div class="grid grid-4"><div class="card step"><b>1</b><h3>Requirement Review</h3><p>Analyze charging power, connector, protocol, site drawings, standard and project country.</p></div><div class="card step"><b>2</b><h3>Product Matching</h3><p>Select charging piles, group charging systems and controllers based on the project architecture.</p></div><div class="card step"><b>3</b><h3>Technical Proposal</h3><p>Prepare product configuration, datasheets, drawings and quotation support.</p></div><div class="card step"><b>4</b><h3>Production &amp; Delivery</h3><p>Support production inspection, packing, documents and export delivery communication.</p></div></div></div></section>
<section><div class="container"><div class="rfq"><div><span class="kicker">Project RFQ</span><h2>Have a Similar Project?</h2><p>Send your project drawings, charging power, quantity and country. Apex will help prepare a suitable configuration.</p></div><form name="rfq" method="POST" data-netlify="true" netlify-honeypot="bot-field"><input type="hidden" name="form-name" value="rfq"><p hidden><label>Do not fill this out: <input name="bot-field"></label></p><div class="form-grid"><input type="text" name="name" autocomplete="name" placeholder="Name" required><input type="email" name="email" autocomplete="email" placeholder="Email" required><input type="tel" name="phone" autocomplete="tel" placeholder="Phone / WhatsApp" required><input type="text" name="company" autocomplete="organization" placeholder="Company" required><input type="text" name="country" autocomplete="country-name" placeholder="Country" required><select name="interest" class="full" required><option value="" selected disabled>Project Type</option><option>EV Charging Station</option><option>Commercial Building Charging</option><option>Fleet / High-Power Charging</option><option>OEM / ODM Charging Equipment</option></select><input type="text" name="voltage_capacity_power" autocomplete="off" placeholder="Charging Power / Connector / Protocol" required><input type="text" name="quantity_project_scale" autocomplete="off" placeholder="Quantity / Project Scale" required><textarea name="message" placeholder="Project requirements" required></textarea><button class="btn btn-orange full" type="submit">Submit Project RFQ</button></div></form></div></div></section>
</main>
{footer(base)}
</body></html>'''
    write(os.path.join(ROOT, "projects", "index.html"), body)

def render_resources():
    base = "../"
    body = f'''{head("Technical Resources and Documents | Apex Power Systems", "Request Apex product datasheets, charging pile reports, certificate materials and export documentation for project evaluation.", "resources/", base)}
{topbar()}
{header(base)}
<main>
<section class="hero"><div class="container">
<div><div class="crumb"><a href="../">Home</a> / Resources</div><span class="kicker">Technical Resources</span><h1>Documents for Project Evaluation</h1><p>Request product-specific datasheets, test or compliance materials, project reference information and export documentation for your technical and procurement review.</p><div class="actions"><a class="btn btn-orange" href="../contact/">Request Documents</a><a class="btn btn-outline" href="mailto:{EMAIL}">Email Apex</a></div></div>
<div class="hero-media"><img src="../assets/integrated/certificate-01.jpg" alt="Technical certification document available for project evaluation"></div>
</div></section>
<section><div class="container"><span class="kicker">Available On Request</span><h2>Document Categories</h2><p class="lead">Document availability and scope depend on the selected equipment, destination market and project requirements. Contact Apex for the relevant review package.</p><div class="grid">
<article class="card"><h3>Product Catalogs &amp; Datasheets</h3><p>Selection information for charging piles, charging controllers, protocol boards and charging equipment.</p></article>
<article class="card"><h3>Charging Pile Technical Reports</h3><p>Model-specific supporting materials can be provided when charging pile scope is confirmed.</p></article>
<article class="card"><h3>Certificates &amp; Compliance</h3><p>Available certificate or compliance documents for procurement and qualification review.</p></article>
<article class="card"><h3>Project References</h3><p>Relevant capability and application reference information for project discussions.</p></article>
<article class="card"><h3>OEM / ODM Technical Exchange</h3><p>Controller, interface, protocol and customisation information for partner evaluation.</p></article>
<article class="card"><h3>Export &amp; Delivery Support</h3><p>Packing, documentation and international project coordination materials as applicable.</p></article>
</div></div></section>
<section class="soft"><div class="container two-col"><div><span class="kicker">Request Checklist</span><h2>Help Us Send the Right Information</h2><p class="lead">Include the product family, target country, charging power, quantity, applicable standard and document purpose in your inquiry.</p></div><div><span class="kicker">Relevant Product Families</span><div class="pills"><span>Charging Piles</span><span>Charging Controllers</span><span>Protocol Boards</span><span>EV Chargers</span><span>EV Charger Controllers</span></div></div></div></section>
<section><div class="container"><div class="contact-box"><div><span class="kicker">Contact Apex</span><h2>Request a Technical Document Package</h2><p>Tell us which products and project stage you are evaluating so the response can match your requirements.</p><div class="contact-links"><a href="mailto:{EMAIL}">{EMAIL}</a><a href="{WHATSAPP}">WhatsApp: +86 13201571341</a></div></div><a class="btn btn-orange" href="../contact/">Open Request Form</a></div></div></section>
</main>
{footer(base)}
</body></html>'''
    write(os.path.join(ROOT, "resources", "index.html"), body)

def render_certificates():
    base = "../"
    body = f'''{head("Compliance and Certificate Documents | Apex Power Systems", "Request product-specific compliance and certificate documentation from Apex Power Systems for technical qualification and procurement review.", "certificates/", base)}
{topbar()}
{header(base)}
<main>
<section class="hero"><div class="container">
<div><div class="crumb"><a href="../">Home</a> / Certificates</div><span class="kicker">Compliance Documentation</span><h1>Qualification Materials for Your Project Review</h1><p>Apex can support customer evaluation with documentation relevant to the selected product scope, technical requirement and destination market. Confirm required standards during your inquiry.</p><div class="actions"><a class="btn btn-orange" href="../contact/">Request Documents</a><a class="btn btn-outline" href="mailto:{EMAIL}">Email Apex</a></div></div>
<div class="hero-media"><img src="../assets/integrated/production-03.jpg" alt="Charging equipment production capability supporting quality review"></div>
</div></section>
<section><div class="container"><span class="kicker">Documentation Scope</span><h2>Materials Available for Review</h2><p class="lead">Certificate applicability depends on product configuration, contracting entity and target-market requirements. Relevant copies are provided for confirmed procurement discussions.</p><div class="grid">
<article class="card"><h3>Quality Management Materials</h3><p>Documentation supporting supplier qualification discussions where applicable to the confirmed scope.</p></article>
<article class="card"><h3>Product Compliance Information</h3><p>Technical and compliance-related materials matched to selected equipment and project requirements.</p></article>
<article class="card"><h3>Testing Documentation</h3><p>Available test or inspection information supplied against an identified product and specification.</p></article>
<article class="card"><h3>Technical Datasheets</h3><p>Electrical parameters, configuration details and drawings for approved product selection.</p></article>
<article class="card"><h3>Export Documentation</h3><p>Supporting documentation for international procurement and delivery coordination as applicable.</p></article>
<article class="card"><h3>OEM / ODM Evaluation</h3><p>Technical review support for partners discussing customised charging or control equipment.</p></article>
</div></div></section>
<section class="soft"><div class="container two-col"><div><span class="kicker">Before Requesting</span><h2>Specify the Intended Use</h2><p class="lead">State your product family, model or electrical scope, country, required standard, tender stage and documentation checklist so Apex can respond accurately.</p></div><div><span class="kicker">Products Supported</span><div class="pills"><span>Charging Piles</span><span>Charging Controllers</span><span>Protocol Boards</span><span>EV Chargers</span><span>Charging Equipment</span></div></div></div></section>
<section><div class="container"><div class="contact-box"><div><span class="kicker">Contact Apex</span><h2>Request Compliance Materials</h2><p>Submit your project and document requirements for a product-specific review package.</p><div class="contact-links"><a href="mailto:{EMAIL}">{EMAIL}</a><a href="{WHATSAPP}">WhatsApp: +86 13201571341</a></div></div><a class="btn btn-orange" href="../contact/">Open Request Form</a></div></div></section>
</main>
{footer(base)}
</body></html>'''
    write(os.path.join(ROOT, "certificates", "index.html"), body)

def main():
    for p in PRODUCTS:
        render_product(p)
    for s in SOLUTIONS:
        render_solution(s)
    render_products_index()
    render_solutions_index()
    render_ev_chargers_controllers()
    render_about()
    render_quality()
    render_contact()
    render_projects()
    render_resources()
    render_certificates()

if __name__ == "__main__":
    main()
