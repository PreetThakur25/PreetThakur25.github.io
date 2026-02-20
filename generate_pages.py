import re
import os

def generate_page(theme_name, accent_color, accent_muted, new_nav, title, subtitle, projects, filename):
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace accent colors
    content = re.sub(r'--accent: #[0-9A-Fa-f]+;', f'--accent: {accent_color};', content)
    content = re.sub(r'--accent-muted: rgba\([^)]+\);', f'--accent-muted: {accent_muted};', content)

    # Replace navigation
    content = re.sub(r'<nav class="fixed.*?</nav>', new_nav, content, flags=re.DOTALL)

    # We want to keep the layout but change the "Major Deployments" title and remove other sections if needed.
    # Let's just remove the Hero, About, Hardware, Contact sections and only keep Navigation, Projects, and Footer.
    
    # Extract Navigation, Projects section, and Footer
    nav_match = re.search(r'(<nav.*?</nav>)', content, flags=re.DOTALL)
    footer_match = re.search(r'(<footer.*?</footer>)', content, flags=re.DOTALL)
    
    # We will build a new body
    head_match = re.search(r'(<head>.*?</head>)', content, flags=re.DOTALL)
    
    # Update title
    head_content = head_match.group(1).replace('<title>PPSB | AI & Embedded Systems Engineer</title>', f'<title>PPSB | {theme_name}</title>')

    project_html = ""
    for idx, proj in enumerate(projects):
        delay = idx * 100
        project_html += f"""
                <div class="project-card reveal group cursor-pointer" onclick="window.location.href='project.html?file={proj['readme'].replace(' ', '%20')}'" style="transition-delay: {delay}ms;">
                    <div class="flex justify-between items-start mb-10">
                        <span class="mono text-[10px] text-[var(--accent)] font-bold tracking-[0.2em]">{proj['tag']}</span>
                        <div class="w-8 h-8 rounded-full border border-white/10 flex items-center justify-center group-hover:bg-[var(--accent)] group-hover:text-black transition-all">
                            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path d="M9 5l7 7-7 7" stroke-width="2" />
                            </svg>
                        </div>
                    </div>
                    <h3 class="text-2xl font-bold mb-4">{proj['name']}</h3>
                    <p class="text-zinc-400 text-sm leading-relaxed mb-8">{proj['desc']}</p>
                    <div class="flex flex-wrap gap-3">
                        {"".join([f'<span class="px-3 py-1 bg-white/5 text-[10px] mono text-zinc-300">{tag}</span>' for tag in proj['tech']])}
                    </div>
                </div>
"""

    projects_section = f"""
    <section id="projects" class="py-24 md:py-40 px-6 min-h-screen">
        <div class="max-w-7xl mx-auto mt-20">
            <div class="mb-20 reveal active">
                <h2 class="text-5xl font-bold uppercase mb-6 tracking-tighter">{title}</h2>
                <p class="text-zinc-500 max-w-2xl leading-relaxed">{subtitle}</p>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                {project_html}
            </div>
        </div>
    </section>
"""

    full_html = f"""<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
{head_content}
<body class="bg-grid">
{new_nav}
{projects_section}
{footer_match.group(1)}
    <script>
        const observerOptions = {{ threshold: 0.1, rootMargin: '0px 0px -50px 0px' }};
        const observer = new IntersectionObserver((entries) => {{
            entries.forEach(entry => {{ if (entry.isIntersecting) entry.target.classList.add('active'); }});
        }}, observerOptions);
        document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
    </script>
</body>
</html>
"""

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(full_html)
    print(f"Generated {filename}")

new_nav = """
    <nav class="fixed top-0 w-full z-50 glass border-b border-white/5">
        <div class="max-w-7xl mx-auto px-6 py-5 flex justify-between items-center">
            <a href="index.html" class="text-xl font-bold mono text-[var(--accent)] tracking-tighter">PREET_PRATAP_</a>
            <div class="hidden md:flex space-x-8 text-[10px] font-bold uppercase tracking-[0.3em]">
                <a href="index.html" class="hover:text-yellow-500 transition-colors">01. Hardware</a>
                <a href="ml.html" class="hover:text-cyan-400 transition-colors">02. ML</a>
                <a href="agents.html" class="hover:text-green-500 transition-colors">03. Agents</a>
                <a href="apps.html" class="hover:text-purple-400 transition-colors">04. Apps</a>
            </div>
        </div>
    </nav>
"""

# ML Page
ml_projects = [
    {
        "tag": "01_TEXT_SUMMARIZER",
        "name": "Text Summarizer Web App",
        "desc": "An AI-powered web app that extracts and summarizes text from PDFs, images, and text files using Hugging Face transformers.",
        "tech": ["Python", "Flask", "HuggingFace", "OCR"],
        "readme": "README text_summrizer.md"
    },
    {
        "tag": "02_SPEECH_TO_TEXT",
        "name": "Speech to Text Engine",
        "desc": "A robust speech-to-text pipeline for offline and online audio processing.",
        "tech": ["Python", "Whisper", "PyAudio"],
        "readme": "README speech_to_text.md"
    }
]
generate_page("ML Projects", "#22d3ee", "rgba(34, 211, 238, 0.2)", new_nav, "Machine Learning", "Intelligence powered by data. Exploring NLP, Computer Vision, and Audio Processing.", ml_projects, "ml.html")

# Agents Page
agents_projects = [
    {
        "tag": "01_REASONING_AGENT",
        "name": "Reasoning Agent",
        "desc": "An advanced autonomous agent capable of chain-of-thought reasoning to solve complex multi-step problems.",
        "tech": ["Python", "LangChain", "LLMs"],
        "readme": "README reasoning_agent.md"
    },
    {
        "tag": "02_ARIP_ENGINE",
        "name": "ARIP Engine",
        "desc": "Core engine for Autonomous Reasoning and Intent Parsing, designed for scalable agentic workflows.",
        "tech": ["Python", "Agentic Framework"],
        "readme": "README arip_engine.md"
    },
    {
        "tag": "03_ARIP",
        "name": "ARIP Application",
        "desc": "The main ARIP interface bringing autonomous reasoning to everyday tasks.",
        "tech": ["Python", "FastAPI"],
        "readme": "README arip.md"
    }
]
generate_page("Agentic Projects", "#22c55e", "rgba(34, 197, 94, 0.2)", new_nav, "Agentic Systems", "Autonomous AI agents and reasoning engines pushing the boundaries of AI capabilities.", agents_projects, "agents.html")

# Apps Page
apps_projects = [
    {
        "tag": "01_SERVERLESS_APP",
        "name": "Serverless App Architecture",
        "desc": "A scalable serverless application built using modern cloud infrastructure and microservices.",
        "tech": ["AWS", "Node.js", "Serverless"],
        "readme": "README serverless_app.md"
    },
    {
        "tag": "02_PRESONTOR_AI",
        "name": "Presontor AI",
        "desc": "An intelligent presentation assistant leveraging AI to generate and format slide decks dynamically.",
        "tech": ["Python", "Generative AI", "APIs"],
        "readme": "README presontor_ai.md"
    }
]
generate_page("App Projects", "#a855f7", "rgba(168, 85, 247, 0.2)", new_nav, "Applications", "Full-stack web applications and scalable cloud solutions.", apps_projects, "apps.html")

