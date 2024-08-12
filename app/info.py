"""
This module defines the context dictionary used to render HTML templates.
"""

context = {
    'name': 'Lovinson Dieujuste 🔥',
    'role': 'Site Reliability Engineer',
    'title': 'My Personal Portfolio',
    'about': (
        'From a young age, I was captivated by coding, '
        'first discovering my passion in elementary school. '
        'Watching a programmer control sprites in an Angry Birds simulation '
        'ignited my desire to master this skill. '
        'Throughout high school, I enthusiastically enrolled in programming electives, '
        'tackled challenges like directing '
        'robots, and experimented with web apps, data structures, and HTML/CSS. '
        'My curiosity led me to mobile game '
        'development, and at 17, I published my first 2D multiplayer shooter. '
        'Despite initial rejection from the Play Store '
        'due to my age, I successfully launched my app on my 18th birthday. '
        'I then expanded my skills to backend technologies, '
        'building comprehensive web applications. Now, as a CS major, '
        'I continue to pursue my passion with enthusiasm, driven '
        'by my achievements and the lessons learned, eager to grow into the '
        'software engineer I\'ve always aspired to be.'
    ),
    'work': 'Work Experience',
    'work_experiences': [
        {
            'title': 'Site Reliability Engineer',
            'company': 'MLH Fellowship',
            'start_date': 'June 2024',
            'end_date': 'Sep 2024',
            'responsibilities': [
                'Developed an open-source web app with Python, Flask',
                ('Completed a 12-week SRE curriculum, '
                 'supplemented with events and workshops by Meta engineers')
            ]
        },
        {
            'title': 'Tech Fellow',
            'company': 'CodePath',
            'start_date': 'May 2024',
            'end_date': 'Aug 2024',
            'responsibilities': [
                ('Answered 100+ technical questions on '
                 'Slack and during breakout sessions'),
                ('Taught in 30+ breakout room sessions and encouraging the use of the '
                 'UMPIRE method, resulting in a 70% improvement in problem-solving efficiency')

            ]
        }
    ],
    'hobby': 'Hobbies',
    'hobbies': [
        {
            'name': 'Binge Watching',
            'image': ['./static/img/Power Book II.jpeg'],
            'description': (
                ('I enjoy watching a variety of topics on Netflix, from science fiction to action. '
                 'My favorite book is "Power Book II".')
            )
        },
        {
            'name': 'Gaming',
            'image': ['./static/img/Brawlhalla.jpeg',
                      './static/img/Madden.jpeg', './static/img/2k24.jpeg'],
            'description': (
                ('I love playing multiplayer games with my friends. Some of the games '
                 'I love to play include Brawlhalla, Madden, and 2k24.')
            )
        }
    ],
    'education': 'Education',
    'education_entries': [
        {
            'degree': 'Computer Science Major',
            'institution': 'University of Tampa, Tampa FL',
            'graduation_date': 'Expected Graduation: 2026',
            'details':
                ('Relevant Coursework: Data Structures and Algorithms, Discrete Math, '
                 'Computer Architecture, Operating Systems, Software Engineering')


        }
    ],
    'places': 'Places',
    'aboutData':  [
      {
        'title': "Frontend",
        'icons': [ "HTML5", "CSS3", "Javascript", "React", "TailwindCSS", "Next.js",
                  "Vite.js", "Framer", "Typescript", "Flask"],
      },
      {
        'title': "Backend",

        'icons': [
           "PostgreSQL", "MongoDB", "MySQL", "Supabase",
           "Node.js", "C#", "Python", "Prisma", "Nginx"],
      },
      {
        'title': "Testing/Deployment",
        'icons': [

           "Heroku", "Verce.js", "Aws", "Jest", "Mocha", "Docker"
        ],
      },
      {
        'title': "Developer Tools",
        'icons': ["Git", "npm", "Webpack", "Babel", "Jinja", "Prometheus", "Grafana"],
      },
      {
        'title': "Technologies",
        'icons': ["Unity", "OAuth", "Firebase", "ChakraUI", "Socket.io", "Cloudinary" ],
      },
    ],
  }
