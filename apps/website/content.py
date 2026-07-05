"""Static site content for the personal website.

This replaces the former database-backed models (``Paragraph`` / ``Service`` /
``WorkHistory``). Edit this file to change the bio, services, or recent works.
There is no admin panel and no database for site content.
See ``.claude/skills/site-content/SKILL.md`` for guidance.

Fields mirror the old models so templates need no changes:
  service: id, title, serial, show, image_url, image_path, video_url,
           description, side_para_top, side_para_middle, side_para_bottom,
           body_text
  work:    same, plus ``category``; no ``side_para_bottom``

- Set ``show=False`` to hide an entry without deleting it.
- ``serial`` controls sort order (ascending).
- ``description`` is plain text (shown on the home page cards).
- ``body_text`` / ``side_para_*`` are raw HTML (rendered with ``|safe``).
"""


def _visible(items):
    return sorted(
        (i for i in items if i.get("show", True)),
        key=lambda i: i["serial"],
    )


def _by_id(items, obj_id):
    for i in items:
        if str(i["id"]) == str(obj_id):
            return i
    return None


def get_short_bio():
    return SHORT_BIO


def get_services():
    """Visible services, sorted by serial."""
    return _visible(SERVICES)


def get_works():
    """Visible recent works, sorted by serial."""
    return _visible(WORKS)


def get_service(obj_id):
    return _by_id(SERVICES, obj_id)


def get_work(obj_id):
    return _by_id(WORKS, obj_id)



SHORT_BIO = """I'm a Software Engineering Lead, currently working at <a href="https://www.techjays.com/"> Techjays. </a>  I've <b>9+ years</b> of experience in <b>backend engineering</b> — building scalable <b>APIs</b>, server automation, and the systems that power modern web and mobile apps. Strong expertise in <b>Python, Django, FastAPI</b> and <b>AWS</b>, with a deep focus on reliable systems and clean architecture. I'm fluent across the <b>AI/ML</b> ecosystem — from machine learning to <b>LLMs</b> and scalable data pipelines — and passionate about bringing <b>agentic AI</b> into real-world products with frameworks like <b>LangChain</b> and <b>LangGraph</b>. Exploring opportunities that combine backend engineering and AI to build products that matter and systems that deliver real value."""


SERVICES = [
    {
        "id": 5,
        "title": """Technical Leadership""",
        "serial": 0,
        "show": True,
        "image_url": None,
        "image_path": "",
        "video_url": None,
        "description": """I lead engineering and AI teams from idea to production — owning architecture, code quality, delivery and mentoring. Open to Technical Lead and Engineering Manager roles where solid backend engineering meets applied AI.""",
        "side_para_top": "",
        "side_para_middle": "",
        "side_para_bottom": "",
        "body_text": """
<p>
I'm a hands-on engineering leader. Across Techjays, IQVIA, ACI and Dingi I've led teams of Python, AI and full-stack engineers — coordinating delivery, setting technical direction, and helping people do their best work.
</p>
<h3>What I bring to a team</h3>
<ul>
    <li>Technical direction and architecture for backend and AI/LLM systems</li>
    <li>Delivery leadership — turning roadmaps into shipped, reliable software</li>
    <li>Code quality, reviews and engineering practices (testing, CI/CD)</li>
    <li>Mentoring engineers and coordinating cross-functional teams</li>
    <li>Bridging product and engineering so effort lands where it creates value</li>
</ul>
<p>
Recent examples: leading a team of AI engineers building LLM-driven solutions at Techjays, coordinating a Python/AI team on GenAI products at IQVIA, and guiding AI teams at ACI. The <a href="/website/projects/">Projects</a> section shows the kind of work my teams and I ship.
</p>
<p>
<b>I'm currently open to Technical Lead and Engineering Manager roles.</b>
</p>
""",
    },
    {
        "id": 6,
        "title": """Rapid MVP Development""",
        "serial": 2,
        "show": True,
        "image_url": None,
        "image_path": "",
        "video_url": None,
        "description": """Have an idea that needs to become a real product fast? As a solo builder I take ideas from zero to a deployed, full-stack MVP — backend, AI and cloud — the way I built ChatExpense and ScanFixNow.""",
        "side_para_top": "",
        "side_para_middle": "",
        "side_para_bottom": "",
        "body_text": """
<p>
Sometimes you don't need a whole team — you need one experienced builder who can take an idea from zero to a working, deployed product. That's something I genuinely enjoy and have done repeatedly on my own.
</p>
<h3>Products I've built solo</h3>
<ul>
    <li><b>ChatExpense</b> — an AI-powered expense tracker (Django, DRF, PostgreSQL, OpenAI, LangGraph); grew to 1300+ registered users with a Google Play app.</li>
    <li><b>ScanFixNow</b> — QR-code-based maintenance incident logging for appliances and installations.</li>
    <li><b>stocksurferbd</b> — a published Python library for Dhaka & Chittagong stock-exchange data.</li>
    <li><b>Wapptel</b> — a WhatsApp marketing-automation platform.</li>
</ul>
<p>
I cover the full stack: backend and APIs, AI/LLM features, database design, and cloud deployment (Docker, AWS, Railway). If you have an MVP to validate quickly, I can help you get it in front of real users. See the <a href="/website/projects/">Projects</a> section for more.
</p>
""",
    },
    {
        "id": 4,
        "title": """Business Growth""",
        "serial": 5,
        "show": True,
        "image_url": None,
        "image_path": "",
        "video_url": None,
        "description": """Modern SEO, AI-driven marketing, optimized sales funnels, and smart lead generation are key to growing your digital business. With analytics and automation, you can boost visibility, attract quality leads, and scale faster in today’s competitive market.""",
        "side_para_top": "",
        "side_para_middle": "",
        "side_para_bottom": "",
        "body_text": """
<p> If your business is growing in the digital space, you already know how crucial visibility and smart marketing are. But as competition heats up, simply being present isn’t enough—you need to be strategic, data-driven, and adaptive. That’s where modern SEO, AI-powered marketing, and optimized sales funnels come in. Leveraging these tools is key to capturing and converting the right audience for your business. </p> 
<h3>Modern SEO</h3> 

<p> Getting found by your ideal customer online is more sophisticated than ever. Modern SEO goes beyond keywords—it's about technical health, authoritative content, and search intent. I can help you audit your website, fix ranking blockers, and implement advanced strategies like schema markup and content clustering so your business climbs higher in search results and attracts high-quality visitors. </p> 

<blockquote> “The best place to hide a dead body is page two of Google.” <br> — Anonymous </blockquote> 

<h3>AI-Powered Social Media Marketing</h3> 

<p> Today’s social media landscape moves at lightning speed. AI can help you analyze trends, schedule and personalize content, and engage the right audience at the right time—automatically. With AI-powered tools, we’ll turn your social channels into active, targeted lead machines, helping your brand stay relevant, responsive, and ahead of the curve. </p> 

<blockquote> “Content is fire, social media is gasoline.” <br> — Jay Baer </blockquote> 

<h3>Sales Funnel Optimization</h3> 

<p> If you’re driving traffic but not seeing enough conversions, it’s time to fine-tune your sales funnel. By mapping the customer journey and optimizing each touchpoint, I can help you turn curious visitors into loyal customers. From landing page tweaks to automated nurturing sequences, you’ll see more value from every lead. </p> 

<blockquote> “Make your funnel work for you, not the other way around.” <br> — Unknown </blockquote> <h3>Lead Generation</h3> 

<p> It’s not just about getting more leads—it’s about getting the right ones. Using smart targeting, automation, and data-driven insights, I can set up systems to attract and qualify prospects who are most likely to buy. Whether it’s inbound, outbound, or AI-enhanced lead generation, let’s fill your pipeline with quality opportunities. </p>

 <blockquote> “Quality over quantity: that’s the mantra of effective lead generation.” <br> — Brian Halligan, Co-founder, HubSpot </blockquote> 

<ul> <li>SEO audits and technical optimization</li> 
<li>AI-driven social media content and scheduling</li> 
<li>Custom sales funnel design and automation</li> 
<li>Targeted lead gen with CRM integration</li> 
</ul>
""",
    },
    {
        "id": 1,
        "title": """Backend Engineering""",
        "serial": 3,
        "show": True,
        "image_url": None,
        "image_path": "",
        "video_url": None,
        "description": """Got an innovative idea for profitable business? Great! Or, have an MPV(Minimum Viable Product) perhaps to show for? Even better!! Now you need present it to the potential clients. That's where I can help you!""",
        "side_para_top": "",
        "side_para_middle": "",
        "side_para_bottom": "",
        "body_text": """
<p>
Got an innovative idea for profitable business? Great! Or, have an MPV(Minimum Viable Product) perhaps to show for? Even better!! Now you need present it to the potential clients. That's where I can help you! Or may be, you already have a business but feeling the need to increase the ROI by decreasing manual labor with some automation? Let's see if we can solve those issues together.
</p>
<h3>Dynamic Portfolio Site</h3>
<p>Dynamic sites are fun! And not that much expensive as you are made to believe! I use the suitable tool set well curated for your needs. You'll get the full control and capability to maintain and update your content with minimal effort. No more 'theme update hell's!
</p>
<blockquote>
"Master online branding. Online branding makes you known for something specific by people who have not even seen you physically, before."
<br>
― Israelmore Ayivor, Shaping the dream
</blockquote>

<h3>E-commerce/Inventory Management</h3>
<p>
Have a running shop/restaurant/service? It's high time you have an online presence. Make you customers life easier with a web portal for browsing you products, place orders and make purchases. Manage your orders and inventory with dynamic admin panels. Collect yous user's contact info and send marketing email. All of those can contribute to scaling your sales! Let me know how can I help you with those.
</p>
<blockquote>
"Create a link through which you can market your dream products. Create a blog or a website of your own depending on what you want to be recognized for. Share your experiences through these media."
<br>
― Israelmore Ayivor, Shaping the dream
</blockquote>

<h3>API Backend/Server automation</h3>
<p>
If you are a developer and need help with API development and server automation I'm here to help. May be you have an app that's got some traction and now you need help to scale up you API Back-End, I can assist you to scale your services. My technology stack-
</p>
<ul>
    <li>Django, Python for API/Backend development</li>
    <li>HTML5, Bootstrap, CSS for static pages</li>
    <li>SPA(Single Page Application) development with React</li>
    <li>MySQL, PostgreSQL, MongoDB.</li>
    <li>Gunicorn, Nginx, Celery for server & automation</li>
    <li>Deployment in AWS, Digital Ocean, Heroku</li>
    <li>Containerization with Docker</li>
</ul>
<p>
I can help you achieve full abstraction for the backend APIs so that you can focus on your web/mobile app development. You also have the option to collaborate in developing parts of the Back-End modules.
</p>
""",
    },
    {
        "id": 3,
        "title": """AI & LLM Engineering""",
        "serial": 1,
        "show": True,
        "image_url": None,
        "image_path": "",
        "video_url": None,
        "description": """Agentic AI empowers systems to act autonomously, pursue goals, and make context-aware decisions. AI agents are essential for next-generation automation and intelligent business solutions. If you need agentic AI system for your business, let’s discuss how I can help turn your vision into reality.""",
        "side_para_top": "",
        "side_para_middle": "",
        "side_para_bottom": "",
        "body_text": """
<p> If you’re exploring the cutting edge of AI automation and agentic workflows, you’ve probably heard about the power of large language models. Maybe you already see the potential of building intelligent assistants or automating complex business processes, but bridging that vision to a working system can be daunting. That’s where I come in: I help you transform your ideas into reality using frameworks like LangChain and LangGraph within the vibrant Python AI ecosystem. </p> <h3>Designing AI-Powered Workflows</h3> 

<p> If you have a specific workflow, task, or assistant concept in mind and want to go beyond simple chatbots, I can help you design robust agentic systems. With LangChain and LangGraph, we can build AI agents that interact with your data, APIs, and tools—making context-aware decisions and orchestrating multi-step processes. Whether it’s a customer support bot, document automation, or intelligent data pipelines, I’ll turn your requirements into reliable, scalable Python solutions. </p> <blockquote> “AI is not just about automating tasks, it’s about building systems that can reason, plan, and adapt. The future belongs to agentic AI.” <br> ― Andrew Ng </blockquote> <h3>Integrating with Python Ecosystem</h3> 


<p> Already using Python for your business logic or data science projects? I can seamlessly integrate LangChain, LangGraph, and other leading AI tools with your existing stack. From connecting LLMs to databases and APIs, to creating custom pipelines and deploying in production, I’ll help you leverage the full power of Python’s mature ecosystem. </p> 

<blockquote> “Python’s versatility and the explosion of AI frameworks have made it the language of choice for modern automation.” <br> ― Sebastian Raschka </blockquote> 

<p> To bring your AI ideas to life, I work with the best-in-class tools and libraries: </p> 

<ul> 
<li>LangChain and LangGraph for agentic AI workflows</li> 
<li>OpenAI, Hugging Face Transformers, LlamaIndex for LLM integration</li> 
<li>FastAPI, Django for web and API interfaces</li>
<li>PostgreSQL, MongoDB, Redis for data and context management</li> 
<li>Vector stores: Pinecone, Weaviate, ChromaDB for retrieval-augmented generation (RAG)</li> 
</ul>
""",
    },
    {
        "id": 2,
        "title": """Automated Trading""",
        "serial": 3,
        "show": False,
        "image_url": None,
        "image_path": "",
        "video_url": None,
        "description": """If you are familiar with the world of online trading, then the need of automated trading system is not news to you! Automate the tedious stuff to well curated scripts and focus more on gathering insights  that enhances your trading portfolio.""",
        "side_para_top": "",
        "side_para_middle": "",
        "side_para_bottom": "",
        "body_text": """
<p>
If you are familiar with the world of online trading, then the need of automated trading system is not news to you! You might have some knowledge and insights regarding the types of trading you do in online brokers. Now you want incorporate those knowledge in your day trading while making buy/sell decisions. I'm here to implement those logic in scripts provide the system for automation.
</p>
<h3>Trading rule implementation</h3>
<p>
If you have the trading logic set up and using those manually through the tool provided by your broker, I can help you to fully automate the process! If your broker provides trading API that support Python/Java/C#/C++ then I can implement desktop/browser tools so that you can trade by just clicking come buttons! Get in touch to discuss in details.
</p>
<blockquote>
“A lot of people get so enmeshed in the markets that they lose their perspective. Working longer does not necessarily equate with working smarter. In fact, sometimes is the other way around.”
<br>
― Martin Schwartz
</blockquote>

<h3>Back-testing Trading Rules</h3>
<p>
You might have come up with some ideas that you think can make you some money out of trading. Now you need battle test those ideas and trough proper back-testing before investing real money on those. I have the proper tools under the belt to help you achieve that.
</p>
<blockquote>
“A peak performance trader is totally committed to being the best and doing whatever it takes to be the best. He feels totally responsible for whatever happens and thus can learn from mistakes. These people typically have a working business plan for trading because they treat trading as a business.”
<br>
― Van K. Tharp
</blockquote>

<p>
Being successful in automated trading is all about using the tools, staying out of emotional impulses and abstracting the technical stuff to the experts. My technology stack-
</p>
<ul>
    <li>Python, C#, MATLAB, C++, Java for API integration</li>
    <li>Experienced IB(Interactive Broker) APIs</li>
    <li>Used IBridgePy library with IB TWS</li>
    <li>Used Quantopian for back-testing.</li>
</ul>
""",
    },
]


WORKS = [
    {
        "id": 1,
        "title": """ChatExpense""",
        "serial": 0,
        "show": True,
        "category": "",
        "image_url": """https://chatexpense-landing-page.s3.us-west-2.amazonaws.com/images/chatexpense_web.jpg""",
        "image_path": """para_images/slide1.png""",
        "video_url": None,
        "description": """ChatExpense is my latest brain-child, an AI-powered personal finance assistant that helps users effortlessly track and manage their spending. Users can log expenses through voice, text, or photos of receipts — and our AI automatically categorizes transactions, identifies spending patterns, and generates personalized insights.""",
        "side_para_top": "",
        "side_para_middle": "",
        "body_text": """
<p>
<img src="https://chatexpense-landing-page.s3.us-west-2.amazonaws.com/images/chatexpense_web.jpg" alt="">
</p>
<p>
<br>
<a href="https://chatexpense.com/">ChatExpense Web app</a>
</br>
<br>
<a href="https://play.google.com/store/apps/details?id=com.chatexpense.app&hl=en">ChatExpense Android app</a>
</br>
</p>
<p>
Beyond simple tracking, ChatExpense is your AI-powered financial assistant. It goes beyond just logging expenses — offering smart insights, spending patterns, future predictions, personalized deals, and investment suggestions based on your financial behavior.
</p>
<p>
Since launch, ChatExpense has grown to <b>1300+ registered users</b> on the web and <b>100+ installs</b> on the Google Play Store, cutting expense-logging time by up to <b>70%</b> through multimodal (text, voice, and receipt-image) input.
</p>

<h3>Product USP</h3>
<p>
ChatExpense brings effortless financial management to everyday users. From chat-based logging to automated categorization, voice input, and receipt scanning — it's a complete solution that works across text, image, and audio. The app empowers users with visual analytics and proactive financial advice without the hassle of spreadsheets or clunky apps.
</p>

<h3>My Contributions</h3>
<p>
As the creator and technical lead of ChatExpense, I was involved in every aspect of the product journey — from the idea stage to a production-ready application. My key contributions include:
</p>
<ul>
    <li>Ideated and developed the core concept of ChatExpense from scratch to address personal finance friction points.</li>
    <li>Built the full backend using Django REST Framework with async support and PostgreSQL.</li>
    <li>Integrated OpenAI APIs for voice, chat, and image-based expense entry and analysis.</li>
    <li>Developed AI agents using LangGraph and LangChain for insight generation, chart building, and smart query handling.</li>
    <li>Deployed on Railway with secure, scalable cloud setup, including Stripe/Bkash payment integrations.</li>
    <li>Led a small team of mobile, backend, and UI/UX developers to push forward feature velocity and user experience.</li>
    <li>Ran targeted marketing campaigns, validated user demand, and prepared for YC application to scale globally.</li>
</ul>
""",
    },
    {
        "id": 2,
        "title": """Followr""",
        "serial": 0,
        "show": False,
        "category": "",
        "image_url": None,
        "image_path": """para_images/followr_desktop.png""",
        "video_url": None,
        "description": "",
        "side_para_top": "",
        "side_para_middle": "",
        "body_text": "",
    },
    {
        "id": 3,
        "title": """Dingi Map APIs""",
        "serial": 1,
        "show": True,
        "category": "",
        "image_url": """https://farhad-portfolio.s3.us-west-2.amazonaws.com/dingi_map_api.jpg""",
        "image_path": """para_images/map_api.png""",
        "video_url": None,
        "description": """Dingi Map API is a platform that helps web service providers to focus on their location based solutions easily with a very reasonable price including tailored custom tailored Map APIs/SDKs. The solution includes a JavaScript Map API and SDK and corresponding Android SDK.""",
        "side_para_top": "",
        "side_para_middle": "",
        "body_text": """
<a href="https://www.dingi.tech/api.php">Dingi Map API Documentation </a>
<br></br>
<p>
Dingi Map API is a platform that helps web service providers to focus on their location based solutions easily with a very reasonable price including tailored custom tailored Map APIs/SDKs. The solution includes a JavaScript Map API and SDK and corresponding Android SDK.
</p>
<h3>Product USP</h3>
<p>
Dngi enhanced map, sdk & services contains detailed information of every areas, suburbs, roads, points of interests, home addresses (currently in Dhaka city), landmarks of Bangladesh. Using dingi map API will enable you to be precise about serving your customer. Also, by using dingi SDK you can tailor our map to your specific needs. Do expect that we will continue to amaze you with further enhancement.
</p>

<h3>My Contributions</h3>
<p>
The initiail version of Dingi Map plaformI was not production ready and not easy to scale. I transformed this MVP like product so that it is able to generate some significant revenue. Here are my contributions-  
</p>
<ul>
    <li>Refactored the whole code base to reduce file system I/O</li>
    <li>Reduced server cost by 50% and improved scalibility and performance by using optimized combination of uWSGI, Nginx.</li>
    <li>Optimized infrastructure and Deployed the Back-End in AWS Cloud using AWS ELB and Autoscaling.</li>
    <li>Introduced the principles of Test Driven Development which was not there from the start</li>
    <li>Scaled out the Map API platform to handle a few hundredrequests per second and cater to the need of high profile clients like Shohoz.com.</li>
</ul>
""",
    },
    {
        "id": 4,
        "title": """Hazard Reporting System""",
        "serial": 2,
        "show": True,
        "category": "",
        "image_url": """https://raw.githubusercontent.com/skfarhad/hazard_reporting_system/refs/heads/main/live_dashboard.jpeg""",
        "image_path": """para_images/search-1.png""",
        "video_url": None,
        "description": """SMS Based Hazard Reporting System for Flood Affected people of Bangladesh""",
        "side_para_top": """
<p>
<img src="https://raw.githubusercontent.com/skfarhad/hazard_reporting_system/refs/heads/main/architecture_roadmap.jpg" alt="" 
style="height: 520px; width: 520px;">
</p>
""",
        "side_para_middle": "",
        "body_text": """
<p>
The Hazard Reporting System is an SMS-based emergency communication platform designed to facilitate rapid reporting and coordinated rescue operations in Bangladesh during natural disasters like floods. It empowers distressed individuals in remote or high-density areas to report emergencies using basic mobile phones, enabling real-time volunteer coordination and geo-tracked rescue missions.
</p>




<p>
<img src="https://raw.githubusercontent.com/skfarhad/hazard_reporting_system/refs/heads/main/HMS_tech_stack.jpg" alt="">
</p>
<h3>Product USP</h3>
<p>
Unlike traditional emergency systems that rely on voice calls or internet access, this platform uses simple SMS technology integrated with geolocation parsing and telco infrastructure (GP, Robi, Banglalink) to reach even the most underserved regions. The system matches distressed individuals with the nearest volunteers using automated backend logic and displays all reports on a live GIS-enabled dashboard. This allows law enforcement, administrative bodies, and trained volunteers to act promptly, saving critical response time.
</p>

<h3>My Contributions</h3>
<p>
As the founder and technical architect of the Hazard Reporting System, I initiated and led the transformation from idea to a working prototype. Here are my key contributions:
</p>
<ul>
    <li>Designed the system architecture to integrate SMS servers, geolocation services, and real-time dashboards for flood-related emergency response.</li>
    <li>Developed backend APIs to manage incidents and volunteer information, using Django and PostgreSQL.</li>
    <li>Integrated Google Maps API and offline GPS parsing tools to resolve and validate locations from SMS texts.</li>
    <li>Built background services to automatically match reported incidents with nearby registered volunteers based on distance and availability.</li>
    <li>Developed a secure web portal for volunteer registration, incident validation, and admin coordination with real-time GIS visualization.</li>
    <li>Collaborated with telco vendors to prototype SMS-to-database pipelines and simulate emergency loads during peak times.</li>
    <li>Conducted user research and field testing in flood-prone areas to validate assumptions and ensure system usability in real-life emergencies.</li>
</ul>
""",
    },
    {
        "id": 5,
        "title": """stocksurferbd""",
        "serial": 3,
        "show": True,
        "category": "",
        "image_url": """https://raw.githubusercontent.com/skfarhad/stocksurferbd/refs/heads/main/price_plot_1d.png""",
        "image_path": "",
        "video_url": None,
        "description": """
This is a Python library based on beautifulsoup4, pandas & mplfinance.
You may use it to download price history and fundamental information of companies from Dhaka Stock Exchange and Chittagong Stock Exchange.
""",
        "side_para_top": "",
        "side_para_middle": "",
        "body_text": """
<a href="https://pypi.org/project/stocksurferbd/">stocksurferbd Python Library Documentation</a>
<br></br>

<p>
    <b>stocksurferbd</b> is a Python package built using <code>beautifulsoup4</code>, 
    <code>pandas</code>, and <code>mplfinance</code> that helps you collect and analyze stock 
    market data from the Dhaka Stock Exchange (DSE) and Chittagong Stock Exchange (CSE). 
    It enables users to download historical prices, fundamental data, and visualize price 
    movements using candlestick charts.
</p>

<h3>Product USP</h3>
<p>
    The package provides a simple and programmatic interface for gathering both real-time 
    and historical stock data from Bangladeshi stock markets. It’s especially useful for 
    investors, data scientists, and finance researchers who want to automate their workflow 
    and analyze stocks in Python without relying on expensive or manual data extraction methods.
</p>

<p>
    <b>Key features include:</b>
</p>
<ul>
    <li>Download historical price data for any listed company in DSE or CSE</li>
    <li>Fetch real-time market data for all listed companies</li>
    <li>Access and save fundamental data (company info, year-wise financials)</li>
    <li>Generate professional-grade candlestick charts using <code>mplfinance</code></li>
</ul>

<h3>My Contributions</h3>
<p>
    I created the entire <b>stocksurferbd</b> package as a personal initiative to make 
    Bangladeshi stock market data accessible for retail investors and analysts. 
    Here are the highlights of my contributions:
</p>
<ul>
    <li>Scraped, cleaned, and structured data from the official DSE and CSE websites using BeautifulSoup</li>
    <li>Built a robust API wrapper for downloading and saving data in Excel format</li>
    <li>Implemented candlestick plotting logic using <code>mplfinance</code> to visualize trends</li>
    <li>Designed easy-to-use interfaces for both beginners and experienced Python users</li>
    <li>Published the library to PyPI and ensured ease of installation via <code>pip install stocksurferbd</code></li>
</ul>

<h3>Sample Usage</h3>

<pre><code>
# Downloading historical price data
from stocksurferbd import PriceData

loader = PriceData()
loader.save_history_data(symbol='ACI', file_name='ACI_history.xlsx', market='DSE')
</code></pre>
<p>
    This will create an Excel file with historical price data for ACI Ltd from DSE.
</p>

<pre><code>
# Downloading fundamental data
from stocksurferbd import FundamentalData

loader = FundamentalData()
loader.save_company_data('ACI', path='company_info')
</code></pre>
<p>
    This will create two Excel files for ACI: one for current fundamental data 
    and one for year-wise financials.
</p>

<pre><code>
# Generating candlestick chart
from stocksurferbd import CandlestickPlot

cd_plot = CandlestickPlot(csv_path='ACI_history.xlsx', symbol='ACI')
cd_plot.show_plot(data_n=120, resample=True, step='3D')
</code></pre>
<p>
    This will generate a 3-day resampled candlestick chart for the most recent 120 data points.
</p>
""",
    },
    {
        "id": 6,
        "title": """ScanFixNow""",
        "serial": 6,
        "show": True,
        "category": "",
        "image_url": """https://scanfixnow-landing-page.s3.us-west-2.amazonaws.com/images/scnfixnow_onboarding.jpg""",
        "image_path": "",
        "video_url": None,
        "description": """QR-Powered Maintenance Logging.  Scan. Report. Fix. Simplify maintenance tracking with QR-code based incident reporting.""",
        "side_para_top": "",
        "side_para_middle": "",
        "body_text": """
<p><img src="https://scanfixnow-landing-page.s3.us-west-2.amazonaws.com/images/scanfixnow_workflow.jpg" alt="How ScanFixNow Works"></p>

</p>
<p>
<br>
<a href="https://scanfixnow.com/">ScanFixNow Web app</a>
</br>
</p>

<p>
<br>🛠 ScanFixNow Overview</br>
<ul>
<li>ScanFixNow is a QR-code-based web app for logging maintenance incident reports. The core idea is to:
Allow customers (like building managers or residents) to scan a QR code placed on lifts, motors, generators, or other appliances.</li>


<li>Upon scanning, they are taken to a web form where they can report an issue (e.g., “Lift not working,” “Generator making noise”).</li>


<li>The data goes to the appliance vendor/service provider, who can then track and manage repair tickets.</li>

</ul>
</p>

<p>
Why Use ScanFixNow?<br/>

<ul>
<li>QR-Scan Logging: 
Scan a code, describe the issue, and submit. It’s that easy. </li>

<br>Faster Response:
Real-time alerts to technicians with priority tracking.</br>

<li>Track Installations:
See all equipment sites on a map and view history by location.</li>

<li>Secure Data:
All data is encrypted and backed by enterprise security practices. </li>
<ul>
</p>

<blockquote>
Ensuring high quality maintenance work should be the focus, data logging will be handled by ScanFixnow!
</blockquote>
""",
    },
    {
        "id": 7,
        "title": """Wapptel""",
        "serial": 4,
        "show": True,
        "category": "",
        "image_url": """/static/website/assets/images/wapptel_service.png""",
        "image_path": "",
        "video_url": None,
        "description": """Small and medium businesses want to run WhatsApp marketing campaigns without paying for the official WhatsApp Business API. Wapptel gives them bulk messaging, contact management and campaign tracking on top of WhatsApp Web — with the safety rails (rate limiting, phone validation) to avoid getting numbers banned.""",
        "side_para_top": "",
        "side_para_middle": "",
        "body_text": """
<p>
<a href="https://wapptel.com/">Wapptel</a>
</p>
<p>
The official WhatsApp Business API is expensive and slow to get approved for a small business that just wants to send a bulk promotion to its customer list. Wapptel solves that by automating WhatsApp Web itself — connect an account by scanning a QR code, then manage contacts, run bulk-messaging campaigns and track delivery from a dashboard, without touching Meta's paid API.
</p>
<h3>How it works</h3>
<ul>
    <li>A three-tier design: a browser SPA talks to a Django backend, which talks to a separate Node.js microservice that holds the actual WhatsApp Web session.</li>
    <li>Campaigns accept an Excel/CSV recipient list, validate Bangladeshi phone numbers, and send with rate limiting and progress tracking to keep accounts from being flagged as spam.</li>
    <li>Multi-tenant from the start — organizations, users and subscriptions are first-class, not bolted on later.</li>
</ul>
<h3>Technology</h3>
<p>
Django REST Framework with JWT and API-key auth, PostgreSQL (+PostGIS), Celery and django-redis for background work, drf-spectacular for API docs, and Stripe for subscription billing. The WhatsApp connection itself is a Node.js/Express microservice built on <code>@whiskeysockets/baileys</code> (WhatsApp Web protocol), with Socket.IO for live QR/connection status and PM2 for process management. LangChain/LangGraph on top of OpenAI power smarter reply and campaign-content features.
</p>
<h3>My Contributions</h3>
<ul>
    <li>Designed the three-tier architecture and built the Django backend end-to-end.</li>
    <li>Built the Node.js/Baileys microservice for WhatsApp Web connection and messaging.</li>
    <li>Implemented the bulk-campaign feature — recipient upload, phone validation, rate-limited sending and progress tracking.</li>
    <li>Set up Celery-based background processing and Stripe subscription billing.</li>
</ul>
""",
    },
    {
        "id": 8,
        "title": """MarketWiki BD""",
        "serial": 7,
        "show": True,
        "category": "",
        "image_url": """/static/website/assets/images/marketwiki_bd.png""",
        "image_path": "",
        "video_url": None,
        "description": """Retail investors in Bangladesh's DSE/CSE market have no easy way to spot pump-and-dump schemes or gauge how trustworthy an issuer is before investing. MarketWiki BD is a market-intelligence platform I'm building to score issuer credibility and flag manipulation patterns automatically.""",
        "side_para_top": "",
        "side_para_middle": "",
        "body_text": """
<p>
<a href="https://marketwikibd.com/">MarketWiki BD</a>
</p>
<p>
Bangladesh's stock market (DSE/CSE) has a long history of syndicate-driven pump-and-dump schemes and opaque issuer practices, and retail investors have no accessible tool to see the warning signs before they're already holding the bag. MarketWiki BD is my answer to that gap — a surveillance and scoring platform that turns public market data and filings into an early-warning signal.
</p>
<h3>What it does</h3>
<ul>
    <li>Computes an Issuer Trust/Authenticity Score from market and disclosure data.</li>
    <li>Classifies manipulation phases and fingerprints syndicate trading patterns.</li>
    <li>Flags influencer-driven pump activity and tracks political/regulatory risk signals.</li>
</ul>
<h3>Technology</h3>
<p>
Django REST Framework backend with JWT/API-key auth and drf-spectacular for the API layer; Channels/Daphne and Celery/RabbitMQ for real-time and background processing; PostgreSQL today, with TimescaleDB, Neo4j and a vector store planned for time-series and relationship analysis. Market data comes in through my own <a href="/website/work-details/?id=5">stocksurferbd</a> library, with pandas for analysis and LangChain (Anthropic/OpenAI/Gemini) for document parsing and pattern reasoning. Stripe handles billing; the whole stack is Dockerized and deployed on Railway.
</p>
<p>
<b>Status:</b> pre-MVP — the product design and core infrastructure (auth, billing, data ingestion scaffolding) are in place; the manipulation-detection models are what I'm building next.
</p>
""",
    },
    {
        "id": 9,
        "title": """High Command""",
        "serial": 8,
        "show": True,
        "category": "",
        "image_url": """/static/website/assets/images/highcommand_game.png""",
        "image_path": "",
        "video_url": None,
        "description": """Turn-based strategy games running game logic separately on the server and in the browser risk the two falling out of sync — letting a client desync into an unfair or exploitable state. High Command is a deterministic, real-time strategic wargame where the same core rules engine runs, verifiably identically, on both sides.""",
        "side_para_top": "",
        "side_para_middle": "",
        "body_text": """
<p>
<a href="https://highcommand.live/">High Command</a>
</p>
<p>
High Command is a two-player, turn-based strategic wargame — missiles, drones and jammers versus interceptors, fighters, radar and civil defence, played out over budgeted 5-turn phases. The interesting engineering problem isn't the game itself, it's keeping the rules engine trustworthy: if the server and the browser ever compute a different outcome for the same move, the game is exploitable.
</p>
<h3>How it's built</h3>
<ul>
    <li>A single Python "core" module holds all deterministic game logic — no duplicated rules on the client.</li>
    <li>That core is compiled to JavaScript with Transcrypt so the browser runs the exact same logic, not a reimplementation.</li>
    <li>A parity test suite runs the same game states through both the Python and compiled-JS versions and diffs the results, catching any behavioral drift.</li>
    <li>Django Channels over WebSockets drives real-time turn exchange between players; Celery/RabbitMQ handle asynchronous processing.</li>
</ul>
<h3>Technology</h3>
<p>
Django + DRF + Channels/Daphne on the backend, PostgreSQL and Redis for state and queuing, Celery/RabbitMQ for background work. The frontend is a pixi.js 8 canvas renderer built with esbuild. Dockerized, deployed on Railway.
</p>
<p>
<b>Status:</b> in active development — the deterministic core, Python/JS parity testing and real-time turn infrastructure are built; game content and matchmaking are in progress.
</p>
""",
    },
]
