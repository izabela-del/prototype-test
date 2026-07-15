import cairosvg
def sun(i): return f'<defs><radialGradient id="su{i}" cx="40%" cy="34%" r="70%"><stop offset="0%" stop-color="#FFF6D0"/><stop offset="52%" stop-color="#FFD24D"/><stop offset="100%" stop-color="#FBB114"/></radialGradient></defs><circle cx="50" cy="50" r="42" fill="#FFDE7A" opacity="0.35"/><circle cx="50" cy="50" r="30" fill="url(#su{i})"/><ellipse cx="41" cy="40" rx="12" ry="9" fill="#fff" opacity="0.5"/>'
def moon(i): return f'<defs><radialGradient id="mo{i}" cx="38%" cy="34%" r="72%"><stop offset="0%" stop-color="#FDFBFF"/><stop offset="100%" stop-color="#CDD1F2"/></radialGradient><mask id="mc{i}"><rect width="100" height="100" fill="black"/><circle cx="50" cy="50" r="30" fill="white"/><circle cx="64" cy="40" r="25" fill="black"/></mask></defs><circle cx="50" cy="50" r="40" fill="#C9CCF4" opacity="0.25"/><circle cx="50" cy="50" r="30" fill="url(#mo{i})" mask="url(#mc{i})"/>'
def cell(i,label,glow,orbx,orby,night):
    W,H=340,238
    orb=moon(i) if night else sun(i)
    stars=''
    if night:
        for sx,sy in [(40,26),(78,16),(120,34),(250,22),(300,40)]:
            stars+=f'<circle cx="{sx}" cy="{sy}" r="1.6" fill="#fff"/>'
    smiley='<g><circle cx="8" cy="8" r="8" fill="#3DAE76"/><circle cx="6" cy="7" r="1.4" fill="#12603D"/><circle cx="10" cy="7" r="1.4" fill="#12603D"/><path d="M5 9.5 Q8 12 11 9.5" fill="none" stroke="#12603D" stroke-width="1.5" stroke-linecap="round"/></g>'
    plus='<g><rect x="6.5" y="1.5" width="3.5" height="13" rx="1.7" fill="#5D6FE8"/><rect x="1.5" y="6.5" width="13" height="3.5" rx="1.7" fill="#5D6FE8"/></g>'
    return f'''
    <text x="0" y="-9" font-family="Georgia, serif" font-size="14" font-weight="700" fill="#4A4A63">{label}</text>
    <clipPath id="cl{i}"><rect x="0" y="0" width="{W}" height="{H}" rx="16"/></clipPath>
    <rect x="0" y="0" width="{W}" height="{H}" rx="16" fill="#F6F6F9" stroke="#E3E3EC"/>
    <g clip-path="url(#cl{i})">
      <filter id="bg{i}" x="-60%" y="-60%" width="220%" height="220%"><feGaussianBlur stdDeviation="20"/></filter>
      <filter id="bo{i}" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="1.4"/></filter>
      <ellipse cx="{orbx+25}" cy="{orby+18}" rx="140" ry="130" fill="{glow}" filter="url(#bg{i})" opacity="0.8"/>
      <g filter="url(#bo{i})">{stars}<g transform="translate({orbx},{orby}) scale(0.46)">{orb}</g></g>
    </g>
    <text x="20" y="52" font-family="Georgia, serif" font-size="27" font-weight="700" fill="#17172B">Hi Carol!</text>
    <text x="20" y="76" font-family="Helvetica, Arial, sans-serif" font-size="13" fill="#4A4A63">To-dos below are based on your action plan.</text>
    <rect x="16" y="96" width="{W-32}" height="{H-112}" rx="14" fill="#fff" stroke="#EAEAF0"/>
    <rect x="30" y="110" width="30" height="30" rx="9" fill="#5B86E8"/><text x="34" y="130" font-family="Helvetica" font-size="15" fill="#fff">℞</text>
    <text x="70" y="118" font-family="Helvetica, Arial, sans-serif" font-size="13.5" font-weight="700" fill="#17172B">How are you feeling on the medication?</text>
    <text x="70" y="136" font-family="Helvetica, Arial, sans-serif" font-size="12" fill="#4A4A63">A quick daily check keeps you safe.</text>
    <rect x="30" y="152" width="128" height="34" rx="17" fill="#fff" stroke="#EAEAF0"/><g transform="translate(42,161)">{smiley}</g>
    <text x="64" y="173" font-family="Helvetica, Arial, sans-serif" font-size="12.5" font-weight="700" fill="#4A4A63">I’m doing well</text>
    <rect x="168" y="152" width="140" height="34" rx="17" fill="#fff" stroke="#EAEAF0"/><g transform="translate(180,161)">{plus}</g>
    <text x="202" y="173" font-family="Helvetica, Arial, sans-serif" font-size="12.5" font-weight="700" fill="#4A4A63">Log side effects</text>'''
cells=[("Dawn · 6am","rgb(255,150,120)",34,20,False),("Midday · 12pm","rgb(255,236,168)",150,8,False),("Sunset · 6:30pm","rgb(255,150,105)",256,20,False),("Night · 10pm","rgb(120,120,185)",258,16,True)]
W,H=340,238; gap=30; cols=2; sheetW=cols*W+(cols+1)*gap; sheetH=2*(H+34)+gap
parts=[]
for i,(lab,glow,ox,oy,night) in enumerate(cells):
    cx=gap+(i%cols)*(W+gap); cy=gap+18+(i//cols)*(H+44)
    parts.append(f'<g transform="translate({cx},{cy})">{cell(i,lab,glow,ox,oy,night)}</g>')
svg=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {sheetW} {sheetH}"><rect width="{sheetW}" height="{sheetH}" fill="#ECECF2"/>{"".join(parts)}</svg>'
cairosvg.svg2png(bytestring=svg.encode(), write_to="sky-stills.png", output_width=sheetW*2, output_height=sheetH*2)
for i,(lab,glow,ox,oy,night) in enumerate(cells):
    one=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W+40} {H+50}"><rect width="{W+40}" height="{H+50}" fill="#ECECF2"/><g transform="translate(20,34)">{cell(i,lab,glow,ox,oy,night)}</g></svg>'
    cairosvg.svg2png(bytestring=one.encode(), write_to="sky-"+lab.split(" ")[0].lower()+".png", output_width=(W+40)*2, output_height=(H+50)*2)
print("done")
