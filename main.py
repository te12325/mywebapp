import streamlit as st

# 1. Page Config
st.set_page_config(
    page_title="AERION JETS — Private Aviation Redefined",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Advanced Custom CSS, Typography, and Interactions
st.markdown("""
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@300;400;500;600&family=Inter:wght@200;300;400;500&display=swap" rel="stylesheet">

    <style>
        /* Hide Default Streamlit Layout Elements */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .stApp {
            margin: 0;
            padding: 0;
            background-color: #0A0A0B;
            color: #E5E5E5;
            font-family: 'Inter', sans-serif;
            overflow-x: hidden;
        }

        .block-container {
            padding: 0rem !important;
            max-width: 100% !important;
        }

        /* Smooth Scroll behavior */
        html {
            scroll-behavior: smooth;
        }

        /* Typography Customization */
        .font-serif-luxury {
            font-family: 'Cinzel', serif;
        }

        /* Keyframe Animations */
        @keyframes fadeInSlow {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        @keyframes navFadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }

        @keyframes imageZoomSlow {
            from { transform: scale(1.0); }
            to { transform: scale(1.08); }
        }

        @keyframes rotateEarth {
            from { transform: scale(1.05) rotate(0deg); }
            to { transform: scale(1.1) rotate(4deg); }
        }

        .anim-hero-text {
            animation: fadeInSlow 1.8s cubic-bezier(0.16, 1, 0.3, 1) forwards;
        }

        .anim-nav {
            animation: navFadeIn 2s ease-out forwards;
        }

        .hero-bg-anim {
            animation: imageZoomSlow 20s infinite alternate ease-in-out;
            will-change: transform;
        }

        .earth-bg-anim {
            animation: rotateEarth 25s infinite alternate ease-in-out;
            will-change: transform;
        }

        /* Global Destinations Hover Effect CSS */
        .dest-item {
            transition: all 0.5s ease;
            opacity: 0.35;
        }
        .dest-list:hover .dest-item {
            opacity: 0.2;
        }
        .dest-list .dest-item:hover {
            opacity: 1.0 !important;
            transform: translateX(12px);
        }

        /* Destination Background Images Fade Control */
        .dest-bg {
            opacity: 0;
            transition: opacity 0.7s ease-in-out, transform 1s ease-out;
            transform: scale(1.03);
        }
        .dest-item-1:hover ~ .dest-bg-1,
        .dest-item-2:hover ~ .dest-bg-2,
        .dest-item-3:hover ~ .dest-bg-3,
        .dest-item-4:hover ~ .dest-bg-4,
        .dest-item-5:hover ~ .dest-bg-5,
        .dest-item-6:hover ~ .dest-bg-6 {
            opacity: 0.25;
            transform: scale(1.0);
        }

        /* Minimal Scrollbar */
        ::-webkit-scrollbar {
            width: 4px;
        }
        ::-webkit-scrollbar-track {
            background: #0A0A0B;
        }
        ::-webkit-scrollbar-thumb {
            background: #222225;
        }
    </style>
""", unsafe_allow_html=True)

# 3. Streamlit Main HTML Rendering
st.markdown("""
    <!-- NAVIGATION -->
    <nav class="fixed top-0 left-0 w-full z-50 flex justify-between items-center px-6 md:px-16 py-8 mix-blend-difference anim-nav">
        <a href="#" class="font-serif-luxury text-lg md:text-xl text-white tracking-[0.25em] font-semibold">AERION</a>
        <div class="hidden md:flex space-x-12 text-xs tracking-[0.2em] text-gray-300 font-light">
            <a href="#editorial" class="hover:text-white transition-colors duration-300">PHILOSOPHY</a>
            <a href="#fleet" class="hover:text-white transition-colors duration-300">FLEET</a>
            <a href="#specs" class="hover:text-white transition-colors duration-300">SPECIFICATIONS</a>
            <a href="#destinations" class="hover:text-white transition-colors duration-300">DESTINATIONS</a>
        </div>
        <a href="#booking" class="text-[11px] border border-white/40 px-5 py-2.5 tracking-[0.2em] text-white hover:bg-white hover:text-black transition-all duration-500">
            BOOK A FLIGHT
        </a>
    </nav>

    <!-- SECTION 1: HERO SECTION -->
    <section class="relative h-screen w-full flex items-center justify-center overflow-hidden bg-black">
        <div class="absolute inset-0 overflow-hidden">
            <img src="https://images.unsplash.com/photo-1540959733332-eab4deabeeaf?q=80&w=2400&auto=format&fit=crop" 
                 alt="AERION Jet Flight" 
                 class="w-full h-full object-cover opacity-70 hero-bg-anim">
        </div>
        <div class="absolute inset-0 bg-gradient-to-b from-black/30 via-transparent to-black/80"></div>

        <div class="relative z-10 text-center px-4 max-w-5xl mx-auto anim-hero-text">
            <h1 class="font-serif-luxury text-5xl md:text-8xl lg:text-9xl text-white tracking-[0.2em] font-extralight mb-4">
                FLY BEYOND
            </h1>
            <p class="text-xs md:text-sm tracking-[0.3em] text-gray-300 font-light uppercase mb-12">
                Private aviation, redefined.
            </p>
            <div>
                <a href="#booking" class="inline-block border border-white/60 px-8 py-3.5 text-xs tracking-[0.25em] text-white hover:bg-white hover:text-black transition-all duration-500">
                    BOOK A FLIGHT
                </a>
            </div>
        </div>
    </section>

    <!-- SECTION 2: EDITORIAL SECTION -->
    <section id="editorial" class="relative bg-[#FBFBF8] text-[#111113] py-32 md:py-48 px-6 md:px-20 overflow-hidden">
        <div class="max-w-7xl mx-auto relative min-h-[70vh] flex items-center justify-center">
            
            <!-- Center Jet Window Image -->
            <div class="relative w-full max-w-2xl h-[500px] md:h-[650px] z-10 overflow-hidden shadow-2xl">
                <img src="https://images.unsplash.com/photo-1519074069444-1ba4eae16748?q=80&w=1600&auto=format&fit=crop" 
                     alt="Window View" 
                     class="w-full h-full object-cover filter grayscale hover:grayscale-0 transition-all duration-1000 scale-105">
            </div>

            <!-- Overlapping Left Editorial Text -->
            <div class="absolute top-8 left-0 md:left-8 z-20 mix-blend-difference text-white md:text-black">
                <h2 class="font-serif-luxury text-4xl md:text-7xl lg:text-8xl font-light leading-none tracking-wider">
                    WE ARE<br>MOVEMENT
                </h2>
            </div>

            <!-- Overlapping Right Editorial Text -->
            <div class="absolute bottom-8 right-0 md:right-8 z-20 text-right mix-blend-difference text-white md:text-black">
                <h2 class="font-serif-luxury text-4xl md:text-7xl lg:text-8xl font-light leading-none tracking-wider">
                    WE ARE<br>DISTINCTION
                </h2>
            </div>
        </div>
    </section>

    <!-- SECTION 3: THE FLEET -->
    <section id="fleet" class="bg-[#F5F5F2] text-[#111113] py-24 md:py-36 px-6 md:px-16 overflow-hidden">
        <div class="max-w-7xl mx-auto">
            <span class="text-[11px] tracking-[0.3em] text-gray-400 uppercase block mb-4">THE FLEET</span>
            <div class="relative w-full h-[60vh] md:h-[80vh] overflow-hidden mb-8">
                <img src="https://images.unsplash.com/photo-1508614589041-895b88991e3e?q=80&w=2400&auto=format&fit=crop" 
                     alt="Private Aircraft" 
                     class="w-full h-full object-cover transition-transform duration-1000 hover:scale-105">
                
                <div class="absolute bottom-10 left-8 md:left-12 z-10 max-w-md bg-black/30 backdrop-blur-md p-6 text-white border-l border-white/30">
                    <h2 class="font-serif-luxury text-2xl md:text-4xl font-light tracking-wide mb-3">
                        BUILT FOR THE JOURNEY
                    </h2>
                    <p class="text-xs text-gray-200 font-light leading-relaxed mb-6">
                        Exceptional performance, refined comfort, and an uncompromising approach to private aviation.
                    </p>
                    <a href="#specs" class="inline-block text-[10px] tracking-[0.25em] border-b border-white pb-1 hover:text-gray-300 transition-colors">
                        EXPLORE AIRCRAFT
                    </a>
                </div>
            </div>
        </div>
    </section>

    <!-- SECTION 4: AIRCRAFT SPECIFICATIONS (Technical Brochure) -->
    <section id="specs" class="bg-[#FAF9F5] text-[#111113] py-32 px-6 md:px-20 border-t border-gray-200">
        <div class="max-w-7xl mx-auto">
            <span class="text-[11px] tracking-[0.3em] text-gray-400 block mb-16 text-center">TECHNICAL BROCHURE</span>
            
            <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
                <!-- Left Column Specs -->
                <div class="lg:col-span-3 space-y-12 text-left">
                    <div>
                        <p class="text-[10px] tracking-[0.25em] text-gray-400 mb-1">RANGE</p>
                        <p class="font-serif-luxury text-2xl md:text-3xl font-normal">4,500 NM</p>
                    </div>
                    <div>
                        <p class="text-[10px] tracking-[0.25em] text-gray-400 mb-1">CRUISING SPEED</p>
                        <p class="font-serif-luxury text-2xl md:text-3xl font-normal">480 KNOTS</p>
                    </div>
                    <div>
                        <p class="text-[10px] tracking-[0.25em] text-gray-400 mb-1">PASSENGERS</p>
                        <p class="font-serif-luxury text-2xl md:text-3xl font-normal">UP TO 12</p>
                    </div>
                </div>

                <!-- Center Blueprint Drawing -->
                <div class="lg:col-span-6 flex justify-center py-8">
                    <img src="https://images.unsplash.com/photo-1583416750470-965b2707b355?q=80&w=1200&auto=format&fit=crop" 
                         alt="Technical Blueprint Drawing" 
                         class="w-full max-w-lg object-contain filter grayscale contrast-125 opacity-80 mix-blend-multiply transition-opacity duration-1000">
                </div>

                <!-- Right Column Specs -->
                <div class="lg:col-span-3 space-y-12 text-left lg:text-right">
                    <div>
                        <p class="text-[10px] tracking-[0.25em] text-gray-400 mb-1">CABIN LENGTH</p>
                        <p class="font-serif-luxury text-2xl md:text-3xl font-normal">14.05 M</p>
                    </div>
                    <div>
                        <p class="text-[10px] tracking-[0.25em] text-gray-400 mb-1">CABIN HEIGHT</p>
                        <p class="font-serif-luxury text-2xl md:text-3xl font-normal">1.92 M</p>
                    </div>
                    <div>
                        <p class="text-[10px] tracking-[0.25em] text-gray-400 mb-1">CABIN AREA</p>
                        <p class="font-serif-luxury text-2xl md:text-3xl font-normal">28.5 M²</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- SECTION 5: DARK MODE TRANSITION (FLY ANYWHERE) -->
    <section class="relative bg-[#050505] text-white py-36 px-6 md:px-20 overflow-hidden">
        <!-- Earth Background Asset -->
        <div class="absolute inset-0 z-0 flex items-center justify-center opacity-40 pointer-events-none">
            <img src="https://images.unsplash.com/photo-1614728894747-a83421e2b9c9?q=80&w=2000&auto=format&fit=crop" 
                 alt="Earth view from space" 
                 class="w-full h-full object-cover earth-bg-anim">
        </div>
        
        <div class="relative z-10 max-w-7xl mx-auto h-full flex flex-col justify-between min-h-[70vh]">
            <!-- Main Content -->
            <div class="text-center my-auto py-16">
                <h2 class="font-serif-luxury text-4xl md:text-7xl lg:text-8xl tracking-[0.2em] font-extralight mb-4">
                    FLY ANYWHERE
                </h2>
                <p class="text-xs md:text-sm tracking-[0.3em] text-gray-400 font-light uppercase mb-12">
                    TOTAL COMFORT AND CONTROL
                </p>
                <div>
                    <a href="#booking" class="inline-block border border-white/30 rounded-full px-8 py-3.5 text-[11px] tracking-[0.25em] hover:border-white hover:bg-white hover:text-black transition-all duration-500">
                        BOOK THE FLIGHT
                    </a>
                </div>
            </div>

            <!-- Footer Meta Info -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8 border-t border-white/10 pt-8 text-xs font-light text-gray-400">
                <div>
                    <p class="leading-relaxed max-w-xs">
                        Your journey should feel as effortless as your destination.
                    </p>
                </div>
                <div class="md:text-right space-y-1">
                    <p class="hover:text-white transition-colors">info@aerionjets.com</p>
                    <p class="hover:text-white transition-colors">+1 555 000 0000</p>
                </div>
            </div>
        </div>
    </section>

    <!-- SECTION 6: GLOBAL DESTINATIONS (Interactive Hover) -->
    <section id="destinations" class="relative bg-[#0A0A0B] text-white py-32 px-6 md:px-20 overflow-hidden min-h-screen flex items-center">
        <!-- Dynamic Background Layer -->
        <div class="absolute inset-0 pointer-events-none z-0">
            <img src="https://images.unsplash.com/photo-1513635269975-59663e0ac1ad?q=80&w=2000&auto=format&fit=crop" class="dest-bg dest-bg-1 absolute inset-0 w-full h-full object-cover" alt="London">
            <img src="https://images.unsplash.com/photo-1502602898657-3e91760cbb34?q=80&w=2000&auto=format&fit=crop" class="dest-bg dest-bg-2 absolute inset-0 w-full h-full object-cover" alt="Paris">
            <img src="https://images.unsplash.com/photo-1496442226666-8d4d0e62e6e9?q=80&w=2000&auto=format&fit=crop" class="dest-bg dest-bg-3 absolute inset-0 w-full h-full object-cover" alt="New York">
            <img src="https://images.unsplash.com/photo-1512453979798-5ea266f8880c?q=80&w=2000&auto=format&fit=crop" class="dest-bg dest-bg-4 absolute inset-0 w-full h-full object-cover" alt="Dubai">
            <img src="https://images.unsplash.com/photo-1503899036084-c55cdd92da26?q=80&w=2000&auto=format&fit=crop" class="dest-bg dest-bg-5 absolute inset-0 w-full h-full object-cover" alt="Tokyo">
            <img src="https://images.unsplash.com/photo-1525625293386-3f8f99389edd?q=80&w=2000&auto=format&fit=crop" class="dest-bg dest-bg-6 absolute inset-0 w-full h-full object-cover" alt="Singapore">
        </div>

        <div class="relative z-10 max-w-5xl mx-auto w-full text-center">
            <span class="text-[10px] tracking-[0.3em] text-gray-500 block mb-8 uppercase">DESTINATIONS</span>
            
            <div class="dest-list space-y-4 font-serif-luxury">
                <div class="dest-item dest-item-1 text-3xl md:text-6xl tracking-wider cursor-pointer py-1">London</div>
                <div class="dest-item dest-item-2 text-3xl md:text-6xl tracking-wider cursor-pointer py-1">Paris</div>
                <div class="dest-item dest-item-3 text-3xl md:text-6xl tracking-wider cursor-pointer py-1">New York</div>
                <div class="dest-item dest-item-4 text-3xl md:text-6xl tracking-wider cursor-pointer py-1">Dubai</div>
                <div class="dest-item dest-item-5 text-3xl md:text-6xl tracking-wider cursor-pointer py-1">Tokyo</div>
                <div class="dest-item dest-item-6 text-3xl md:text-6xl tracking-wider cursor-pointer py-1">Singapore</div>
            </div>
        </div>
    </section>

    <!-- SECTION 7: BOOKING CTA -->
    <section id="booking" class="bg-[#FBFBF8] text-[#111113] py-36 px-6 md:px-20 text-center border-t border-gray-200">
        <div class="max-w-4xl mx-auto">
            <h2 class="font-serif-luxury text-4xl md:text-7xl font-light tracking-wide leading-tight mb-6">
                WHERE WILL<br>YOU FLY NEXT?
            </h2>
            <p class="text-xs md:text-sm tracking-[0.25em] text-gray-500 font-light uppercase mb-12">
                Begin your private aviation experience.
            </p>
            <div>
                <a href="mailto:concierge@aerionjets.com" 
                   class="inline-block bg-[#111113] text-white px-12 py-5 text-xs tracking-[0.3em] border border-transparent hover:bg-transparent hover:text-black hover:border-black transition-all duration-500 hover:scale-105">
                    BOOK A FLIGHT
                </a>
            </div>
        </div>
    </section>

    <!-- FOOTER -->
    <footer class="bg-[#050505] text-gray-600 py-12 px-6 md:px-20 text-[10px] tracking-[0.25em]">
        <div class="max-w-7xl mx-auto flex flex-col md:flex-row justify-between items-center space-y-4 md:space-y-0">
            <div class="font-serif-luxury text-white text-sm">AERION JETS</div>
            <div>&copy; 2026 AERION JETS AG. ALL RIGHTS RESERVED.</div>
            <div class="flex space-x-6">
                <a href="#" class="hover:text-white transition-colors">PRIVACY</a>
                <a href="#" class="hover:text-white transition-colors">TERMS</a>
            </div>
        </div>
    </footer>
""", unsafe_allow_html=True)
