import base64
#input = {'search': "environmental", 'parameters': {'location': "california", 'genre': "Technology", }, 'organizations': []}

def search(input):

  output = {'matches': []}
  terms = input['search'].split(" ")
  
  # return every organization if empty search
  if len(input['search']) == 0 or "laremy" in terms:
    output['matches'] = input['organizations']
  
  # checking for organization search by number
  elif len(terms) == 1 and terms[0].isdigit():
    number = int(terms[0])
    for org in input['organizations']:
      if org['number'] == number:
        output['matches'].append(org)
  # adding organizations matching key terms to output
  else:
    for org in input['organizations']:  # for each organization
      org_matches = False
      for key in org:
        for term in terms:
          if term in str(org[key]).lower():  # if a term is found in any of the dict values
            org_matches = True
            break
        if org_matches:
          break
      if org_matches:
        output['matches'].append(org)  # add it to the 'matches' list
        continue
    
  # applying filters
  i = 0
  while i < len(output['matches']):
    org = output['matches'][i]

    # for each parameter, check if org parameter matches, if not -> remove the org
    for key in input['parameters']:
      if key in org:
        if str(org[key]).lower() != str(input['parameters'][key]).lower():
          del output['matches'][i]
          i -= 1
      else:
        del output['matches'][i]
        i -= 1
    i += 1
  return output  # code below is for testing, should be removed on final revision  for match in output['matches']:

# below is an example of a call to the search function

"""orgs = [
    {
      "number": 1,
      "name": "TechSphere Inc.",
      "type": "Technology Consultancy Firm",
      "genre": "Technology",
      "resources": "Cutting-edge software development tools and a team of 50 engineers",
      "contact": {
        "name": "John Smith",
        "position": "CTO",
        "email": "john@techsphere.com"
      },
      "description": "TechSphere Inc. specializes in providing innovative technology solutions through cutting-edge software development tools and a talented team of 50 engineers."
    },
    {
      "number": 2,
      "name": "GreenScape Alliance",
      "type": "Environmental NGO",
      "genre": "Technology",
      "resources": "Network of 500 volunteers, environmental research lab",
      "contact": {
        "name": "Emily Green",
        "position": "Director",
        "email": "emily@greenscape.org"
      },
      "description": "GreenScape Alliance is an Environmental NGO committed to environmental conservation, supported by a network of 500 volunteers and an environmental research lab."
    },
    {
      "number": 3,
      "name": "GlobalHealth Innovations",
      "type": "Healthcare Solutions Provider",
      "genre": "Health",
      "resources": "Medical research facilities, 24/7 medical helpline",
      "contact": {
        "name": "Dr. Mark Johnson",
        "position": "CEO",
        "email": "mark@globalhealth.com"
      },
      "description": "GlobalHealth Innovations focuses on providing healthcare solutions, utilizing medical research facilities and a 24/7 medical helpline under the leadership of Dr. Mark Johnson, the CEO."
    },
    {
      "number": 4,
      "name": "FutureWorks Academy",
      "type": "Education & Training Institute",
      "genre": "Education",
      "resources": "Online learning platform, expert instructors",
      "contact": {
        "name": "Sarah Lee",
        "position": "Head of Partnerships",
        "email": "sarah@futureworks.org"
      },
      "description": "FutureWorks Academy is an Education & Training Institute offering an online learning platform and expert instructors, with Sarah Lee leading partnerships as the Head of Partnerships."
    },
    {
      "number": 5,
      "name": "UrbanBuilders Consortium",
      "type": "Construction and Development Company",
      "genre": "Construction",
      "resources": "Skilled labor force, state-of-the-art equipment",
      "contact": {
        "name": "David Thompson",
        "position": "Project Manager",
        "email": "david@urbanbuilders.net"
      },
      "description": "UrbanBuilders Consortium specializes in construction and development, boasting a skilled labor force and state-of-the-art equipment, managed by Project Manager David Thompson."
    },
    {
      "number": 6,
      "name": "ArtsFusion Collective",
      "type": "Arts and Culture Organization",
      "genre": "Art",
      "resources": "Artist residency program, exhibition spaces",
      "contact": {
        "name": "Rachel Adams",
        "position": "Creative Director",
        "email": "rachel@artsfusion.org"
      },
      "description": "ArtsFusion Collective promotes arts and culture through an artist residency program and exhibition spaces, with Rachel Adams serving as the Creative Director."
    },
    {
      "number": 7,
      "name": "InvestWell Finance Group",
      "type": "Financial Advisory Firm",
      "genre": "Finance",
      "resources": "Investment analysis tools, expert financial advisors",
      "contact": {
        "name": "Michael Reynolds",
        "position": "Senior Financial Analyst",
        "email": "michael@investwellgroup.com"
      },
      "description": "InvestWell Finance Group provides financial advisory services, utilizing investment analysis tools and guided by the expertise of Senior Financial Analyst Michael Reynolds."
    },
    {
      "number": 8,
      "name": "CleanEco Solutions",
      "type": "Sustainable Cleaning Products Manufacturer",
      "genre": "Manufacturing",
      "resources": "Eco-friendly product line, R&D team",
      "contact": {
        "name": "Laura White",
        "position": "Marketing Manager",
        "email": "laura@cleaneco.com"
      },
      "description": "CleanEco Solutions is a manufacturer of sustainable cleaning products, featuring an eco-friendly product line and a dedicated R&D team, led by Marketing Manager Laura White."
    },
    {
      "number": 9,
      "name": "YouthEmpower Network",
      "type": "Youth Development Nonprofit",
      "genre": "Education",
      "resources": "Mentorship programs, youth centers",
      "contact": {
        "name": "Alex Johnson",
        "position": "Program Coordinator",
        "email": "alex@youthempower.org"
      },
      "description": "YouthEmpower Network is a Youth Development Nonprofit focusing on mentorship programs and youth centers, led by Program Coordinator Alex Johnson."
    },
    {
      "number": 10,
      "name": "TechBoost Innovations",
      "type": "Technology Incubator",
      "genre": "Technology",
      "resources": "Startup mentoring, co-working spaces",
      "contact": {
        "name": "Jessica Adams",
        "position": "Innovation Manager",
        "email": "jessica@techboost.com"
      },
      "description": "TechBoost Innovations operates as a Technology Incubator, providing startup mentoring and co-working spaces, with Jessica Adams overseeing innovation as the Innovation Manager."
    },
    {
      "number": 11,
      "name": "FoodShare Foundation",
      "type": "Hunger Relief Organization",
      "genre": "Non-profit",
      "resources": "Food banks, community kitchens",
      "contact": {
        "name": "Sam Patel",
        "position": "Volunteer Coordinator",
        "email": "sam@foodsharefoundation.org"
      },
      "description": "FoodShare Foundation is a Hunger Relief Organization actively involved in providing food banks and community kitchens, managed by Volunteer Coordinator Sam Patel."
    },
    {
      "number": 12,
      "name": "SolarTech Solutions",
      "type": "Renewable Energy Company",
      "genre": "Technology",
      "resources": "Solar panel manufacturing, solar farm installations",
      "contact": {
        "name": "Rachel Carter",
        "position": "Sales Manager",
        "email": "rachel@solar-techsolutions.com"
      },
      "description": "SolarTech Solutions specializes in renewable energy, engaging in solar panel manufacturing and solar farm installations, with Rachel Carter leading sales as the Sales Manager."
    },
    {
      "number": 13,
      "name": "DataInsights Corporation",
      "type": "Data Analytics Firm",
      "genre": "Finance",
      "resources": "Advanced data analysis tools, data scientists",
      "contact": {
        "name": "Steven Lewis",
        "position": "Chief Data Officer",
        "email": "steven@datainsights.co"
      },
      "description": "DataInsights Corporation is a Data Analytics Firm utilizing advanced data analysis tools and a team of skilled data scientists, under the leadership of Chief Data Officer Steven Lewis."
    },
    {
      "number": 14,
      "name": "GlobalEducation Exchange",
      "type": "International Student Exchange Program",
      "genre": "Education",
      "resources": "Network of partner universities, cultural immersion programs",
      "contact": {
        "name": "Maria Rodriguez",
        "position": "Program Director",
        "email": "maria@globaledexchange.org"
      },
      "description": "GlobalEducation Exchange facilitates international student exchange programs, fostering cultural immersion and maintaining a network of partner universities, with Maria Rodriguez as the Program Director."
    },
    {
      "number": 15,
      "name": "HealthFirst Clinics",
      "type": "Medical Clinics Chain",
      "genre": "Health",
      "resources": "Multi-specialty doctors, modern medical facilities",
      "contact": {
        "name": "Dr. Emily Davis",
        "position": "Medical Director",
        "email": "emily@healthfirstclinics.com"
      },
      "description": "HealthFirst Clinics operates a chain of medical clinics, providing multi-specialty medical services in modern facilities, led by Medical Director Dr. Emily Davis."
    },
    {
      "number": 16,
      "name": "EcoHarvest Farms",
      "type": "Organic Farming Cooperative",
      "genre": "Agriculture",
      "resources": "Vast farmlands, sustainable agricultural practices",
      "contact": {
        "name": "Daniel Brown",
        "position": "Farm Manager",
        "email": "daniel@ecoharvestfarms.org"
      },
      "description": "EcoHarvest Farms is an Organic Farming Cooperative managing vast farmlands and implementing sustainable agricultural practices, with Daniel Brown serving as the Farm Manager."
    },
    {
      "number": 17,
      "name": "TechConnect Labs",
      "type": "Research & Development Center",
      "genre": "Technology",
      "resources": "State-funded grants, research partnerships",
      "contact": {
        "name": "Dr. Sarah Johnson",
        "position": "Research Lead",
        "email": "sarah@techconnectlabs.net"
      },
      "description": "TechConnect Labs is a Research & Development Center receiving state-funded grants and engaging in research partnerships, led by Research Lead Dr. Sarah Johnson."
    },
    {
      "number": 18,
      "name": "CommuniCare Foundation",
      "type": "Community Health Services",
      "genre": "Health",
      "resources": "Mobile clinics, health education programs",
      "contact": {
        "name": "Laura Adams",
        "position": "Outreach Coordinator",
        "email": "laura@communicare.foundation"
      },
      "description": "CommuniCare Foundation provides Community Health Services through mobile clinics and health education programs, with Outreach Coordinator Laura Adams coordinating outreach efforts."
    },
    {
      "number": 19,
      "name": "EnviroGuardians",
      "type": "Environmental Protection Group",
      "genre": "Law",
      "resources": "Legal advocacy, environmental policy experts",
      "contact": {
        "name": "Thomas Hughes",
        "position": "Environmental Lawyer",
        "email": "thomas@enviroguardians.com"
      },
      "description": "EnviroGuardians is an Environmental Protection Group specializing in legal advocacy and environmental policy, led by Environmental Lawyer Thomas Hughes."
    },
    {
      "number": 20,
      "name": "FutureTech Innovations",
      "type": "Futuristic Technology Research Institute",
      "genre": "Technology",
      "resources": "AI labs, quantum computing research",
      "contact": {
        "name": "Dr. Alex Chen",
        "position": "Chief Scientist",
        "email": "alex@futuretechinnovations.org"
      },
      "description": "FutureTech Innovations is a Futuristic Technology Research Institute conducting research in AI labs and exploring quantum computing, guided by Chief Scientist Dr. Alex Chen."
    },
    {
      "number": 21,
      "name": "STEMEdge Foundation",
      "type": "STEM Education Advocacy Group",
      "genre": "Non-profit",
      "resources": "Robotics kits, coding workshops",
      "contact": {
        "name": "Karen Foster",
        "position": "Program Manager",
        "email": "karen@stemedgefoundation.org"
      },
      "description": "STEMEdge Foundation is a STEM Education Advocacy Group providing robotics kits and coding workshops, with Karen Foster managing programs as the Program Manager."
    },
    {
      "number": 22,
      "name": "Global Learning Initiative",
      "type": "Educational Content Provider",
      "genre": "Education",
      "resources": "Online learning platforms, interactive courses",
      "contact": {
        "name": "James Collins",
        "position": "Director of Education",
        "email": "james@globallearninginitiative.com"
      },
      "description": "Global Learning Initiative serves as an Educational Content Provider, offering online learning platforms and interactive courses under the guidance of Director of Education James Collins."
    },
    {
      "number": 23,
      "name": "Artistry Academy",
      "type": "Creative Arts School",
      "genre": "Art",
      "resources": "Art studios, masterclasses by renowned artists",
      "contact": {
        "name": "Olivia Turner",
        "position": "Dean of Arts",
        "email": "olivia@artistryacademy.org"
      },
      "description": "Artistry Academy is a Creative Arts School featuring art studios and masterclasses by renowned artists, with Olivia Turner as the Dean of Arts."
    },
    {
      "number": 24,
      "name": "LanguageLink Institute",
      "type": "Language Learning Center",
      "genre": "Education",
      "resources": "Immersive language programs, cultural exchanges",
      "contact": {
        "name": "Miguel Hernandez",
        "position": "Language Program Coordinator",
        "email": "miguel@languagelinkinstitute.com"
      },
     "description": "LanguageLink Institute operates as a Language Learning Center, offering immersive language programs and cultural exchanges, with Miguel Hernandez coordinating language programs."
    },
    {
      "number": 25,
      "name": "FutureSkills Institute",
      "type": "Vocational Training Center",
      "genre": "Education",
      "resources": "Industry partnerships, hands-on training facilities",
      "contact": {
        "name": "Sophia Clark",
        "position": "Career Advisor",
        "email": "sophia@futureskillsinstitute.org"
      },
      "description": "FutureSkills Institute is a Vocational Training Center fostering industry partnerships and providing hands-on training facilities, with Sophia Clark offering career advice as the Career Advisor."
    },
    {
      "number": 26,
      "name": "GreenEarth Education",
      "type": "Environmental Education Nonprofit",
      "genre": "Education",
      "resources": "Nature reserves, sustainability workshops",
      "contact": {
        "name": "Anna White",
        "position": "Environmental Educator",
        "email": "anna@greeneartheducation.org"
      },
      "description": "GreenEarth Education is an Environmental Education Nonprofit managing nature reserves and conducting sustainability workshops, with Anna White serving as the Environmental Educator."
    },
    {
      "number": 27,
      "name": "TechGenius Academy",
      "type": "Technology Education Center",
      "genre": "Technology",
      "resources": "Coding boot camps, tech competitions",
      "contact": {
        "name": "Daniel Lee",
        "position": "Head Instructor",
        "email": "daniel@techgeniusacademy.com"
      },
      "description": "TechGenius Academy is a Technology Education Center offering coding boot camps and tech competitions, led by Head Instructor Daniel Lee."
    },
    {
      "number": 28,
      "name": "Globetrotter Schools Network",
      "type": "International School Network",
      "genre": "Education",
      "resources": "Diverse curriculum, global exchange programs",
      "contact": {
        "name": "Lisa Anderson",
        "position": "Admissions Director",
        "email": "lisa@globetrotterschools.net"
      },
      "description": "Globetrotter Schools Network is an International School Network providing a diverse curriculum and global exchange programs, with Lisa Anderson overseeing admissions as the Admissions Director."
    }
  ]

thingy = {'search': "john", 'organizations': orgs, 'parameters': {}}

print("\n\n\n")

out = search(thingy)

for org in out['matches']:
  print(org['number'])
print("\n\n")

for org in out['matches']:
  print(org)
print("\n\n")"""