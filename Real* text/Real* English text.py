#MenuTitle: English
# -*- coding: utf-8 -*-
# by Pedro Arilla
from __future__ import division, print_function, unicode_literals
__doc__="""
Opens a new tab and outputs Real* English text.

All texts are property of their author(s).
"""

import GlyphsApp, time, random
Glyphs.clearLog()
print("New tab with Real* English text @ " + time.strftime("%H:%M:%S"))

dictionary = [
    "And while her new novel, The Island of Missing Trees — her first since the Booker-shortlisted 10 Minutes 38 Seconds in This Strange World — is certainly political, its themes to do with violence and loss, it’s also a passionate love story, one of whose most important characters just happens to be — yes — a gentle and sagacious tree.",
    "She believes that they can: “You carry a place in your soul, even through the stories you were not told. You can sense the void. The past matters, because it shapes us, whether we know it or not.”",
    "Is she hopeful for the future of Cyprus?",
    "The Island of Missing Trees is published by Penguin (£14.99) on 5 August. To support the Guardian and the Observer preorder your copy at guardianbookshop.com. Delivery charges may apply.",
    "In 2018, upon her return from a trip to China, my roommate gifted me a pack of black surgical masks. Affixed to the plastic packaging was an explanatory note: RAVE MASKS :)",
    "But that’s not now.",
    "Now I’m back in the party. I’m in Ridgewood, I’m in Bushwick, I’m in Bed-Stuy. I run into friends I haven’t seen in over a year, draped in mesh and black latex.",
    "Tokyo’s Olympic architecture: look, no Bird’s Nest…",
    "Eye-catching new buildings will be in short supply when the Tokyo Olympics open next week. Instead, most venues are repurposed — some from the city’s transformative 1964 Games.",
    "Considerable interest has recently been generated by a 3D-animated giant calico creature that mews and wiggles from a newly installed billboard at passengers coming and going from Tokyo’s Shinjuku station.",
    "The quadrennial theatre of ballooning Olympic budgets has reached new levels; some estimates put it at £18.75bn, up from an original budget of £5.26bn. In a recent poll, 83% of Japanese people said they wanted it postponed or cancelled.",
    "Using computer modelling to address these hurdles and accelerate the intensification of cultured meat production is a central goal of the Cultivated Meat Modeling Consortium (CMMC).",
    "Suns Fans Find Meaning—and Connection—in Devin Booker and His Mexican Heritage.",
    "Spend some time in Phoenix—especially lately—and that last sentiment rings true.",
    "Booker is introduced last among the starters during Suns games; he gets the loudest cheers, and his jerseys are ubiquitous. When the team was at its low point, winning 21 and 19 games during the 2016-17 and 2017-18 seasons, Ochoa remembers friends from Sonora asking for tickets to see the visiting Kevin Durant or LeBron James.",
    "Phoenix’s diversity hasn’t made it immune from Arizona’s complicated relationship with Latinos (especially those who have immigrated to the country).",
    "ESPN’s NBA Finals Studio Shows Keep Missing the Point.",
    "Like an aging scout, I watched Wednesday’s halftime show with a timer. First, host Maria Taylor threw it to Jalen Rose. Rose’s spiel (saluting Devin Booker) lasted 9.86 seconds.",
    "As the God of Mischief turned to see the TVA change before his eyes, the final episode of Loki’s first (but not only!) season cruelly cut to black. The journey is over, Loki’s had his heart ripped out, and a new mega-villain has made his debut. Let’s talk about it all.",
    "Subscribe: Spotify / Apple Podcasts / Stitcher / RSS.",
    "Content ©2021 The Garden All Rights Reserved.",
    "Gray Simmons, Founder & Managing Director.",
    "“Giannis took off and he was calling for the ball,” explained Holiday. “I just threw it as high as I could.”",
    "He shook off two quick fouls, after it appeared the Suns would run the Bucks off the floor — they built a 16-point first quarter lead — and helped Milwaukee shoot 32-for-45 in the middle two quarters.",
    "That is changing the contours of the countryside—and of politics.",
    "They will be the first summer games since 1984’s—which were boycotted by the Soviet Union—at which Russia will not be present, at least officially.",
    "$649 for a 512GB NVMe SSD, as well as an anti-glare etched glass screen treatment.",
    "Personally, I love the prospect of being able to seamlessly transition playing PC games between desktop and handheld, and the openness of the platform means I’ll now be able to go mobile with not only my overflowing Steam library (thanks Humble Bundles and Steam Sales) but also all my Epic Games Store, uPlay, and itch.io collections.",
    "Space Jam: A New Legacy gets a modern update to one of nostalgia’s largest strongholds.",
    "LeBron James’ performance is self-deprecating and earnest, if not a bit uneven, but excels when it matters the most, especially against Don Cheadle’s chaotic villain and Cedric Joe’s vulnerable Dom.",
    "Instead, he walked away with a killer deal: The store offered to buy his one-year-old truck for $3,000 more than what he originally paid for it last spring.",
    "“We’ve moved into the more moderate phase of expansion,” said Ellen Zentner, chief U.S. economist at Morgan Stanley.",
    "OPEC+ Agrees to Boost Oil Output as Demand Roars Back.",
    "Producers to increase production by 400,000 barrels a day, moving to restore capacity they cut at the start of the Covid-19 pandemic.",
    "Mandela served 27 years in prison, split between Robben Island, Pollsmoor Prison and Victor Verster Prison.",
    "At the firm, Mandela befriended Gaur Radebe—a Hlubi member of the ANC and Communist Party—and Nat Bregman, a Jewish communist who became his first white friend.",
    "Allahabad Bypass Expressway is an 84.708 km (52.635 mi) access controlled highway located in the district of Allahabad.",
    "A group of American soldiers and Italian partisans during World War II join forces in northern Italy against the Germans.",
    "In February 2019 Reine Minoru came home eleventh of the seventeen runners behind Dea Ragalo in the Kyoto Himba Stakes and was retired from racing.",
    "Factors involved in the development of MCC include the Merkel cell polyomavirus (MCPyV or MCV), a weakened immune system, and exposure to ultraviolet radiation.",
    "Merkel cell carcinoma (MCC) usually presents as a firm nodule (up to 2 cm diameter) or mass (>2 cm diameter).",
    "In December 2018, the U.S. Food and Drug Administration granted accelerated approval to Pembrolizumab (KEYTRUDA®, Merck & Co. Inc.) for all ages (adults and pediatrics) with recurrent locally advanced or metastatic Merkel cell carcinoma.",
    "Stage IA: 80%. Stage IB: 60%. Stage IIA: 60%. Stage IIB: 50%. Stage IIC: 50%. Stage IIIA: 45%. Stage IIIB: 25%. Stage IV: 20%. 5 yr survival may be 51% among people with localized disease, 35% for those with nodal disease, and 14% with metastases to a distant site.",
    "http://www.faqs.org/people-search/strobel-washington/",
    "SM Suzhou is the first SM mall in Jiangsu Province, and the fifth China mall expansion of SM Prime Holdings in the country. It has 72,552 m2 (780,940 sq ft) of retail space.",
    "5G speed. A14 Bionic, the fastest chip in a smartphone. An edge-to-edge OLED display. Ceramic Shield with four times better drop performance. And Night mode on every camera. iPhone 12 has it all — in two perfect sizes.",
    "Blast past fast.",
    "From $29.12/mo. for 24 mo. or $699 before trade‑in.",
    "Both the Wide and Ultra Wide cameras now have Night mode — and it’s better than ever at capturing incredible low-light shots.",
    "iOS 14 is packed with shortcuts that get you just what you want, right when you want it.",
    "Program available for iPhone 12 and iPhone 12 Pro. Available to qualified customers with a credit check and eligible U.S. credit or debit card. Requires a 24-month installment loan with a 0% APR from Citizens Bank, N.A. (subject to any interest, fees, or other costs payable to the card issuer), purchase of AppleCare+ for iPhone, and iPhone activation with one of these national carriers: AT&T, Sprint, Verizon, or T-Mobile. Sales tax and any applicable fees due at time of purchase. Full terms apply.",
    "Data plan required. 5G and LTE are available in select markets and through select carriers. Speeds vary by site conditions and carrier. For details on 5G and LTE support, contact your carrier and see apple.com/iphone/cellular.",
    "Save up to $700 on the newest iPhone after trade‑in.*",
    "Play Has No Limits™.",
    "Experience lightning-fast loading with an ultra-high speed SSD, deeper immersion with support for haptic feedback, adaptive triggers and 3D Audio*, and an all-new generation of incredible PlayStation® games.",
    "Harness the power of a custom CPU, GPU and SSD with Integrated I/O that rewrite the rules of what a PlayStation console can do.",
    "Connect your PlayStation VR to your PS5 console to enjoy supported PS VR games.",
    "© 2020 Sony Interactive Entertainment LLC.",
    "Published in the print edition of the July 26, 2021, issue, with the headline “High Fliers.”",
    "She has been at the magazine since 1995, and, as a senior editor for many years, focussed on national security, international reporting, and features.",
    "A common refrain on Twitter in recent days has been that Bourdain would surely have hated the use of his A.I.-generated voice. ",
    "But we strive for fairness, and the Internet has also made invaluable contributions. For example: during Game Three of the N.B.A. Finals, I mistakenly turned away from the action to do some reading.",
    "Roughly two dozen possible new cases have been reported by U.S. spies and diplomats in the Austrian capital, more than in any other city except Havana itself.",
    "#WeAreOneTeam.",
    "New Premier League kits revealed for 2021/22.",
    "Can be disabled by setting collector.cookie.enabled to false.",
    "Used to identify if the user is in an active session on a site or if this is a new session for a user (i.e. cookie doesn’t exist or has expired).",
    "Guéhi, a 21-year-old centre-back, joins Palace after a season-and-a-half on loan at Championship side Swansea City, where he played 59 games and helped to secure sixth- and fourth-placed league finishes consecutively.",
    "Winning the treble with the Blues’ Under-18s in 2016/17, Guéhi signed his first professional contract in September 2017 and went on to help Chelsea scoop the quadruple – including the FA Youth Cup and league – that same season.",
    "“[The club is taking] a really exciting direction with the new gaffer that’s come in. A lot of good young players are here and obviously such a stable club with top players really enticed me and made me want to come.”",
    "An England international with 19 caps, Bertrand made his top-flight debut as a Chelsea player, where he would help the team lift the UEFA Champions League, UEFA Europa League and Emirates FA Cup.",
    "Speaking to LCFC.com, he said: “I’m really happy to be here; joining Leicester really complemented my inner ambitions and what I still want to achieve in my career. ",
    "He has 19 caps to his name and was part of the squad for UEFA EURO 2016.",
    "The 22-year-old striker spent last season on loan with Belgian side Anderlecht where he scored 21 goals in 41 games across all competitions.",
    "Over 150 participants were benefitting from the scheme by the end of February, with work alongside local charity, SecondBite, offering an additional source of fresh and nutritious food.",
    "The answer is: Janine Beckie.",
    "Now, you may ask yourself: why does US-born Beckie represent Canada?",
    "Though the 28-year-old was born in Highlands Ranch and raised in Saskatchewan (and represented the Untied States at youth level), she was offered the chance to play for the country in which her parents and three brothers were born, and took the opportunity with both hands – or feet.",
    "LIFE: Sean Connery.",
    "Plus: an essay by TIME’s acclaimed film and culture critic Richard Corliss examines how Bond reflects and influences the world at large.",
    "In 1956 Gjon Mili captured her performing in the Broadway musical version of the comic strip Li’l’ Abner. Newmar had the small but memorable role of Stupefyin’ Jones (she would reprise the role in the 1959 film version), whose name embodied the effect she had on men.",
    "Portrait of actress Julie Newmar in Broadway play “The Marriage-Go-Around,” 1958.",
    "Ralph Morse/The LIFE Picture Collection © Meredith Corporation.",
    "Effective Date: March 16, 2017.",
    "In accordance with California Civil Code §1789.3, you may report complaints to the Complaint Assistance Unit of the Division of Consumer Services of the California Department of Consumer Affairs by contacting them in writing at 400 R Street, Sacramento, CA 95814, or by telephone at (800) 952-5210.",
    " You have the right to opt out of the provisions of this Arbitration Agreement by sending a timely written notice of your decision to opt out to the following address: Meredith Corporation, 1716 Locust Street, Des Moines, IA 50309-3023, Attn: General Counsel or email to arbitrationoptout@meredith.com, within 30 days after first becoming subject to this Arbitration Agreement.",
    "Rowland Scherman/National Archive/Newsmakers/Shutterstock.",
    "Bob Dylan and Joan Baez performed during a civil rights rally on August 28, 1963 in Washington D.C.",
    "The following is excerpted from LIFE’s special issue Bob Dylan: America’s Greatest Songwriter, available at newsstands and on Amazon.",
    "Yet many others, indeed the heavy bulk of the public commenters, were thrilled at the choice—both in admiration of Dylan’s writing and also because the committee had shown a willingness to buck tradition and test institutional bias.",
    "“It’s exciting that the Nobel Prize recognizes that.” Billy Collins, America’s former poet laureate, gave his blessing to Dylan’s Nobel. Songwriters cheered for one of the own. (“Holy mother of god,” wrote Rosanne Cash.) Barack Obama tweeted his congratulations.",
    "Why We All Love Lucy.",
    "The 64 members of the St. Lucy’s Cadets drum-and-bugle corps made a formidable sight. Marching with their trumpets, tubas, drums, and flags, the Newark, New Jersey, band blazed through the Hollywood, U.S.A., section of the New York World’s Fair.",
    "And she thrilled to a crowd,” says Kathleen Brady, author of Lucille: The Life of Lucille Ball.",
    "And why not? She’s easy to love.",
    "How to write the perfect modern-day sex scene.",
    "That morning the headlines were full of photos of the 27-year-old pop star with his new girlfriend, 37-year-old Olivia Wilde – also on a yacht.",
    "Email editor@penguinrandomhouse.co.uk and let us know.",
    "Image: Ryan McEachern / Penguin.",
    "In 2019, after publishing three incredible collections of poetry – Burnings (2010), No (2013), and Night Sky with Exit Wounds (2016), the latter of which won the young poet the Whiting Award and the T.S. Eliot prize – poet Ocean Vuong released his heart-breaking debut novel, On Earth We’re Briefly Gorgeous.",
    "We Were Liars by E. Lockhart (2014).",
    "So what are we to make of it all?",
    "Perhaps what The Paper Palace’s ending shows us is that, when we really connect with a book’s characters, it’s not always easy for us to accept the decisions they make.",
    "Product Information: 204mm x 25mm x 138mm; 354g weight.",
    "Select 3 books and get them for the price of £33.",
    "Buy 30 for £330 (RRP £450).",
    "If you not only love having a great classic to read but also cherish the feel of a wonderful object, then these are the books for you. Bound in cloth and each individually designed by Coralie Bickford-Smith.",
    "Jun 08, 2021 | ISBN 9780593188132.",
    "Hardcover: $29.00.",
    "Jack Ryan, Jr., will do anything for a friend, but this favor will be paid for in blood in the latest electric entry in the #1 New York Times bestselling series.",
    "From the renowned author of The African Trilogy, a political satire about an unnamed African country navigating a path between violence and corruption.",
    "Aug 16, 2016 | 160 Pages | 5-3/16 x 8 | ISBN 9780385086165.",
    "“A magical writer—one of the greatest of the twentieth century.” —Margaret Atwood.",
    "More information can be found at  (www.penguin.com) and (www.randomhouse.com).",
    "Penguin Group (USA) is a Penguin Random House Company.  For additional career opportunities, please visit www.penguinrandomhouse.com.",
    "The first book in the #1 bestselling Thursday Murder Club series but TV Presenter Richard Osman.",
    "Thursday 22nd July 12:00 - Sunday 25th July.",
    "£7.49 Paperback.",
    "Joe's Family Food: 100 Delicious, Easy Recipes to Enjoy Together (Hardback).",
    "Put your family first with this cookbook from Joe Wicks, aka The Body Coach, the nation's favourite PE teacher and record-breaking bestselling author.",
    "Dimensions: 254 x 197 x 25 mm.",
    "Marcus Rashford MBE is recognised worldwide for his journey both on and-off the pitch – but how did a boy from the South of Manchester become not only an International footballer but also one of the leading activist voices in the UK?",
    "Longlisted for the Orwell Prize for Political Fiction 2021.",
    "Add an extra layer of security with two -actor authentication (2FA) when logging into GitHub. Require 2FA and choose from TOTP apps, security keys, and more.",
    "Use GPG or S/MIME to sign tags and commits locally. These are marked as verified on GitHub so other people know the changes come from a trusted source.",
    "Access GitHub from your OS X or Windows desktop.",
    "$21 per user/month.",
    "Ready to get started?",
    "GitHub Desktop 2.9 expands the drag-and-drop functionality introduced in Desktop 2.7. You can now squash and reorder commits, start a new branch from an earlier commit, and amend your last commit. If you’re using an Apple Silicon machine with the new M1 chip, Desktop 2.9 also upgrades you to a native build that improves performance and reduces crashes.",
    "GitHub Actions workflow visualizations (#88): track and troubleshoot complex workflows at a glance.",
    "C++20 modules are not supported. We also improved the code scanning API to return the CodeQL query version used for an analysis.",
    "GitHub will be observing a holiday from July 5-9 and on all Fridays in July and August (7/23, 7/30, 8/6, 8/13, 8/20, 8/27) and will have limited staffing during this time.",
    "50,000 automation minutes/month.",
    "Frequently asked questions.",
    "“With GitHub Actions, deployments happen 75 percent faster—taking about 10 minutes compared to the 40 minutes required when they were done manually.”",
    "Meet your developers where they already are. GitHub is home to over 40 million developers and the world’s largest open source community.",
    "You can add a summary of the proposed changes, review the changes made by commits, add labels, milestones, and assignees, and @mention individual contributors or teams.",
    "Draft pull requests are available in public repositories with GitHub Free for organizations and legacy per-repository billing plans, and in public and private repositories with GitHub Team, GitHub Enterprise Server 2.17+, and GitHub Enterprise Cloud.",
    "Millions of teams trust GitHub to keep their work safe.",
    "Universal Second Factor (U2F).",
    "Posted on Jun 29, 07:14 UTC.",
    "Click Use your camera to take a picture.",
    "Dimensions(in) (L x W x H): 8.2 x 5.4 x 1.1.",
    "100 Essential Female Authors.",
    "Shipping: US$ 19.95 (From Canada to Spain).",
    "“A glorious book . . . A spirited defense of science . . . From the first page to the last, this book is a manifesto for clear thought.” —Los Angeles Times.",
    "Condition: New. New. Seller Inventory # Q-0345409469.",
    "© 1996 - 2021 AbeBooks Inc.",
    "Are registered trademarks with the Registered US Patent & Trademark Office.",
    "An ecommerce pioneer, our company was founded in 1995 and our first website, AbeBooks.com, was launched a year later. We're a subsidiary of Amazon.com, Inc. after being acquired in December 2008. Our headquarters are located in Victoria, British Columbia, Canada, and we also have an office in Munich, Germany.",
    "Save up to 90% on your favorite items at BargainBookStores.com! Our 20,000 square foot warehouse in Grand Rapids, Michigan is filled with hundreds of thousands of books and consumer goods, all at the lowest prices!",
    "BargainBookStores guarantees 100% Customer Satisfaction. We ship worldwide and offer a variety of shipping methods to meet your needs.",
    "We accept payment by MasterCard and Visa. For more information, contact us by email at cs@bargainbookstores.com.",
    "Whether you’re a new recruit or a seasoned bounty hunter, the Metroid™ Dread Report series is a great way to go deeper into the upcoming game and the world of Samus Aran.",
    "Happy hunting!",
    "We thank you and look forward to seeing you again!",
    "Whether you're a long-time fan or you're just getting started, Nintendo NY has something for you!",
    "Via Subway B, D, F, M to 47-50 Sts.",
    "Phone: (646) 459-0800.",
    "Today, the Pokémon Company International and TiMi Studio Group announced that the Pokémon UNITE™ game will release this month on July 21, 2021, for Nintendo Switch systems.",
    "To celebrate launch, players who log in to the Nintendo Switch version of Pokémon UNITE by August 31, 2021, will receive a Unite license for Zeraora,* which will allow Trainers to use the Pokémon in battle.",
    "Pokémon UNITE will become available in September 2021 on mobile devices, which will also include language support across both mobile devices and Nintendo Switch in French, Italian, Spanish, and German. For more information about Pokémon UNITE, please visit https://unite.pokemon.com/.",
    "Join Link in his high-flying quest to save Zelda, a childhood friend who must confront her destiny. Soar between floating islands and descend to the treacherous surface world in the earliest story of the Legend of Zelda™ series.",
    "Figure shown not actual size. Visit amiibo.com for details on amiibo functionality.",
    "Get the digital or physical version of the game.",
    "Enter the My Nintendo Legend of Zelda™: Skyward Sword HD Sweepstakes!",
    "Decorate your home or office with this beautiful 24W x 14.5 acrylic panel.",
    "Sweepstakes begins 10:00AM PT on 6/29/2021 and ends at 11:59PM PT on 8/1/2021.",
    "Koholint Island is full of friendly folks—and not-so-friendly monsters.",
    "Hello everyone. I’m Yoshiki Haruhana, and I worked on the graphic direction for this title. The Legend of Zelda: Link’s Awakening was first released on Game Boy™ over 20 years ago, and it’s a game that lots of people still have fond memories of playing. With that in mind, our approach of revamping the graphics was to make sure that we didn’t make them feel ‘forced’.",
    "There are more than 100 Shrines of Trials scattered throughout Hyrule. Link must solve the puzzles inside to prove his heroism and earn in-game rewards.",
    "There’s more to fighting than just weapons, of course. Link will also have to learn a variety of different attacks—like high-flying bow shots and making use of explosives—in order to prevail.",
    "Please select a system to continue...",
    "A credit card is required to use this service and a $0.50 fee is to ensure it is used by an adult.",
    "Review Terms & Conditions.",
    "The economy of California, with a gross state product of $3.2 trillion as of 2019, is the largest sub-national economy in the world.",
    "Nevada is the driest state in the United States.",
    "The average summer diurnal temperature range approaches 40 °F (22 °C) in much of the state.",
    "Nevada's highest recorded temperature is 125 °F (52 °C) at Laughlin on June 29, 1994, and the lowest recorded temperature is −50 °F (−46 °C) at San Jacinto on January 8, 1937.",
    "The scale of the rebellion appeared to be small, so he called for only 75,000 volunteers for 90 days.",
    "He bombarded Fort Sumter on April 12–13, forcing its capitulation.",
    "Washington, D.C., coextensive with the District of Columbia and also known as D.C. or just Washington, is the capital city of the United States.",
    "By 1870, the district's population had grown 75% from the previous census to nearly 132,000 residents.",
    "In Hatod, 16% of the population is under 6 years of age.",
    "Hatod is located at 22.8°N 75.73°E.",
    "Desde el Comienzo: 1994–2004 is a compilation of greatest hits released by the Puerto Rican rock band Fiel a la Vega in 2005.",
    "They are on a list of up to 50,000 phone numbers of people believed to be of interest to clients of the company, NSO, leaked to major news outlets.",
    "NSO denies any wrongdoing.",
    "But with more than 68% of UK adults fully vaccinated modelling suggests hospital admissions, serious illness and deaths from Covid-19 will be at a lower level than in earlier peaks.",
    "Rashid claimed 2-30, fellow leg-spinner Matt Parkinson 1-25 and off-spinner Moeen 2-32 as Pakistan lurched to 155-9.",
    "The price of Brent crude oil is up 43% this year to almost $74 a barrel.",
    "Higher output quotas have also been agreed for several members from May 2022, including the UAE, Saudi Arabia, Russia, Kuwait and Iraq.",
    "Business reporter, BBC News.",
    "The online auction runs until 1 August and is expected to raise £75,000.",
    "Bowie, who died of cancer in 2016, commissioned Mr Bell to design the artwork for 1980's Scary Monsters after going to an exhibition of the artist's work.",
    "Follow BBC West Midlands on Facebook, Twitter and Instagram. Send your story ideas to: newsonline.westmidlands@bbc.co.uk.",
    "This place is England and – more specifically – Cumbria.",
    "In the years afterwards, archaeologists comb through ruined city apartments looking for artefacts from the past – the early 2000s.",
    "MySpace apologised for the data loss at the time.",
    "An introvert’s moment to shine.",
    "A refreshing change of pace.",
    "Emoji?!?",
    "Whether you’re signalling urgency or excitement with ALL CAPS, impatience and irritation with an “?!?” or mutual appreciation with a fist-bump emoji, you are helping your text to convey the feelings you would have embodied in person.",
    "Erica Dhawan’s book Digital Body Language, is out now from St Martin’s Press.",
    "David Robson is the is author of The Intelligence Trap: Revolutionise Your Thinking and Make Wiser Decisions (Hodder & Stoughton/WW Norton) – out now in paperback. He is @d_a_robson on Twitter.",
    "A nomadic future?",
    "One study shows that in mid-2020, the digital-nomad population in the US exploded 50% from 2019, up to 10.9 million from 7.3 million.",
    "The unexpected NFT gold rush.",
    "AJ didn't hold back in today's challenge, snogging Hugo and leaving him feeling a little bit flustered...",
    "Series 7 - Episode 21- As the Islanders continue to enjoy a summer like no other, tonight there are plenty more surprises in store and the competition is on.",
    "© Copyright ITV plc 2018.",
    "Sorry, The Page You Are Looking For Does Not Exist.",
    "Please click here to go home.",
    "Boris Johnson will spend so-called “freedom day” self-isolating after being “pinged” by Test and Trace following a meeting with Health Secretary Sajid Javid, who has tested positive for Covid-19.",
    "Select a continent to access the Peugeot websites you are looking for.",
    "Beauty, balance and bodywork optimized for extreme performance. This is #Peugeot9X8 #Hypercar. Hitting the track at @FIAWEC 2022.",
    "@paugasol Great to see you out there, Pau!",
    "Dame for 3 & the @usabasketball lead!",
    "After a thrilling ending to Game 5, @SamMitchellNBA & @Earl_Watson break down Jrue Holiday's clutch steal and lob on #NBAFinals Film Room.",
    "KD fadeaway. Bucket.",
    "Durant...",
    "After his CLUTCH strip & lob in Game 5.. we showcase some of the best steals of @Jrue_Holiday11's career thus far!",
    "1971 @Bucks Champions Kareem Abdul-Jabbar, Oscar Robertson, Jon McGlocklin & Bob Dandridge, Comedians @DaveChappelle + @christuckerreal & More! @NBA @Suns.",
    "USA Women Can’t Overcome Shooting Woes in Narrow Exhibition Loss to Australia.",
    "LAS VEGAS (July 16, 2021) — There is no panic, just determination to improve.",
    "That is the mindset of the USA Basketball Women’s National Team following a second-straight exhibition loss, a 70-67 setback to Australia on Friday at the Michelob ULTRA Arena at Mandalay Bay in Las Vegas.",
    "Coming off a 93-85 loss to the WNBA All-Stars on Wednesday, the U.S. was hoping to get back on track with another day of practice. But the USA, which will be pursuing its seventh-straight gold medal when the Tokyo Olympic Games begin in a week, had 18 turnovers and shot 37.3% (25-67 FGs) overall and was just 2-of-18 from 3-point.",
    "The U.S. wraps up pre-Olympic play on Sunday, July 18 against Nigeria. The 2:30 p.m. ET game will be on the Olympic Channel: Home of Team USA.",
    "Copyright 2021 NBA Media Ventures, LLC. All rights reserved. No portion of NBA.com may be duplicated, redistributed or manipulated in any form. By accessing any information beyond this page, you agree to abide by the NBA.com.",
    "We want to learn more about you and where you currently stand against those experiences.",
    "To get started, please register if you are first-time user or log in.",
    "Path to Officiating in the NBA, WNBA and G League.",
    "A record 45% of players on start-of-season NBA rosters have played in the G League.",
    "If you'd like to speak to one of our friendly advisors, please contact us on +44 (0) 330 333 0251.",
    "The NBA Store is operated under licence by Fanatics.",
    "We are in the studio Monday to Friday, 9:30am-5:00pm.",
    "Your payments are processed by Stripe.",
    "Millions of businesses of all sizes—from startups to large enterprises—use Stripe’s software and APIs to accept payments, send payouts, and manage their businesses online.",
    "The world’s most powerful and easy-to-use APIs.",
    "Our systems operate with 99.9%+ uptime and are highly scalable and redundant. Stripe is certified to the highest compliance standards.",
    "We offer client and server libraries in everything from React and PHP to .NET and iOS.",
    "The corporate card for fast-growing businesses.",
    "Business name.",
    "Tax Identification Number (if applicable).",
    "Ownership information such as name, date of birth, address, and Social Security number (if applicable, or, for non-U.S. Citizens, documentary verification based on passport or local identification) of all Control Persons and beneficial owners with greater than 25% beneficial ownership in the Applicant. “Control Person” means any individual with control over the Applicant, including a director, general partner or executive officer.",
    "As part of the Stripe Corporate Card application process, we ask that you connect your bank account through the Stripe Dashboard.",
    "The Stripe Corporate Card is currently in Beta and is available via invitation only for U.S. entities.",
    "Celtic Bank, a Utah-chartered Industrial Bank (Member FDIC) issues the Stripe Corporate Card.",
    "You’ll earn unlimited 1.5% cash back on every business purchase you make with the Stripe Corporate Card. We also have additional cash back rewards and other offers with a number of partners. We’ll automatically apply your cash back in the form of a credit on your monthly statement, ensuring that your cash back rewards never go to waste. For additional details, see the Stripe Rewards Program Agreement.",
    "Can I use my Stripe Corporate Card with Apple Pay and Google Pay?",
    "How do I pay my bill?",
    "What happens when I connect my Corporate Card account to Expensify, QuickBooks, or Xero?",
    "And we’re serious about creating amazing products, practices, and open work for all teams.",
    "Introducing our newest event, Collaboratory: A Confluence Series. Discover ways to improve team collaboration during 20 minute weekly episodes starting on August 4.",
    "Powering innovation at 200,000+ companies worldwide.",
    "Educational resources to help take your team to the next level.",
    "Registration for Team '21 is now closed. All Access users will have access until December 31, 2021.",
    "6 weekly episodes starting August 4, 2021.",
    "Your registration provides access to all 6 sessions, though you are not required to watch every session.",
    "Get back to growth with the world’s #1 CRM, powered by Customer 360.",
    "See how Jet It increased sales revenue by 3X with Salesforce.",
    "Since the pandemic, 58% of sales reps think their job has changed forever. Get the latest State of Sales research, based on a survey of leaders, reps, and ops teams around the world.",
    "New research shows how nearly 6,000 sales professionals are selling in a global crisis.",
    "Coming September 21-23, 2021.",
    "President & Chief Product Officer, Salesforce.",
    "4x WNBA Champion, 4x Olympic Gold Medalist, and Athlete Activist.",
    "Our next location may be a surprise, but inspiration is a guarantee.",
    "Salesforce.com, inc. The Landmark @ One Market, Suite 300, San Francisco, CA, 94105, United States.",
    "Available for Mac, iOS, Windows, and Android.",
    "$4.99/yr or $29.99 once — 30-day trial in app.",
    "PDF-Preview.",
    "Apple AppStore App of the Year 2011, 2012, and 2013.",
    "No more than one mail per month.",
    "Academia rarely requires documents to be submitted in .md format. iA Writer has this covered: the app offers HTML, MS Word (.docx) and .pdf export. iA Writer offers the most complete Markdown to Word import/export parsing around.",
    "iOS 14+ and iA Writer Classic (2.1.6).",
    "Users who've updated iOS devices to iOS 14 may experience crashes or inability to open iA Writer Classic (2.1.6).",
    "iA Writer uses the bundle identifier to associate templates with documents. Each template must have a unique identifier. The identifier must contain only alphanumeric (A-Z, a-z, 0-9), hyphen (-), and period (.) characters. The string should be in reverse-DNS format. For example, if your company’s domain is example.com you could assign the string com.example.template as the bundle identifier.",
    "Avoid vertical margins and padding for the document page.",
    "Note that some users may enable accessibility sizes in Settings > General > Accessibility > Larger Text.",
    "2 containers allow you to run 2x parallelism and 2x concurrency.",
    "CircleCI is provided by a third-party and is governed by separate terms of service, privacy policy, and support documentation.",
    "2,000 automation minutes/month.",
    "In 2020, as a company, we raised over $2 million for nonprofits around the world.",
    "Sign up for a non-profit account on us.",
    "Want to get involved?",
    "Subscribe to our RSS feed for updates—we’re excited you’re here with us!",
    "The efficiency or flow of a given day — in other words, interruptions and meetings — has an outstanding impact on whether that day is a good one.",
    "Take a minute to reflect.",
    "The wrap: 10/10 would recommend.",
    "LGBTQIA+ employees at Buck release a zine spotlighting 26 queer people of colour.",
    "See for yourself: The Writing On The Wall premieres today on YouTube.",
    "We last wrote about Shana’s work two years ago, where she explained that she’s been a life-long hoarder and collector, a hobby that has directly inspired her work and fascination with objects.",
    "Are you hoping to pursue a career in the creative industry?",
    "Applicants must have graduated, or be due to graduate, from an undergraduate course (bachelor’s or equivalent) in 2021.",
    "We’re hiring!",
    "The Lead Creative job role is currently in the senior band and we will look to develop the role into the Head-Of (Creative Director) role.",
    "Copyright © It's Nice That, 2021.",
    "The complete PDF productivity solution. Create, sign, share, edit, convert, and export PDFs across desktop, mobile, and web. See how nice it is to go totally digital.",
    "Full featured — full power.",
    "Local, regional, and industry compliance are at the core of Document Cloud. Whether complying with GDPR, eIDAS, FDA 21 CFR Part 11, or FedRAMP, we’ve got your remote workforce covered."
    ]
text = ""
for i in range(5):
    text += random.choice(dictionary) + " "
Font.newTab(text)

print("Tab with Real* English text opened.")
