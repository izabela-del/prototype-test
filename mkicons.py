import cairosvg
smiley = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
 <defs>
  <radialGradient id="g" cx="36%" cy="30%" r="82%">
   <stop offset="0%" stop-color="#CFF6E0"/><stop offset="50%" stop-color="#5FCB93"/><stop offset="100%" stop-color="#249B64"/>
  </radialGradient>
  <radialGradient id="hl" cx="50%" cy="50%" r="50%">
   <stop offset="0%" stop-color="#fff" stop-opacity="0.92"/><stop offset="70%" stop-color="#fff" stop-opacity="0"/>
  </radialGradient>
  <radialGradient id="rim" cx="50%" cy="68%" r="62%">
   <stop offset="60%" stop-color="#12653F" stop-opacity="0"/><stop offset="100%" stop-color="#12653F" stop-opacity="0.38"/>
  </radialGradient>
 </defs>
 <ellipse cx="50" cy="91" rx="30" ry="6" fill="#000" opacity="0.13"/>
 <circle cx="50" cy="48" r="40" fill="url(#g)"/>
 <circle cx="50" cy="48" r="40" fill="url(#rim)"/>
 <ellipse cx="36" cy="31" rx="21" ry="15" fill="url(#hl)"/>
 <ellipse cx="39" cy="47" rx="4.6" ry="6.2" fill="#12603D"/>
 <ellipse cx="61" cy="47" rx="4.6" ry="6.2" fill="#12603D"/>
 <path d="M35 59 Q50 72 65 59" fill="none" stroke="#12603D" stroke-width="5.4" stroke-linecap="round"/>
</svg>'''
plus = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
 <defs>
  <linearGradient id="pg" x1="0" y1="0" x2="0" y2="1">
   <stop offset="0%" stop-color="#B4C4FF"/><stop offset="52%" stop-color="#6E82F0"/><stop offset="100%" stop-color="#4657D6"/>
  </linearGradient>
  <radialGradient id="ph" cx="50%" cy="50%" r="50%">
   <stop offset="0%" stop-color="#fff" stop-opacity="0.8"/><stop offset="65%" stop-color="#fff" stop-opacity="0"/>
  </radialGradient>
 </defs>
 <ellipse cx="50" cy="91" rx="26" ry="5.5" fill="#000" opacity="0.13"/>
 <rect x="39" y="15" width="22" height="70" rx="11" fill="url(#pg)"/>
 <rect x="15" y="39" width="70" height="22" rx="11" fill="url(#pg)"/>
 <ellipse cx="50" cy="33" rx="17" ry="13" fill="url(#ph)"/>
</svg>'''
open("icon-smiley.svg","w").write(smiley); open("icon-plus.svg","w").write(plus)
for n,s in [("icon-smiley",smiley),("icon-plus",plus)]:
    cairosvg.svg2png(bytestring=s.encode(), write_to=n+".png", output_width=256, output_height=256)
# preview strip
prev='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 110"><rect width="220" height="110" fill="#F6F6F9"/><g transform="translate(6,5)">'+smiley.split(">",1)[1].rsplit("</svg",1)[0].replace("<svg","")+'</g></svg>'
print("wrote icons")
