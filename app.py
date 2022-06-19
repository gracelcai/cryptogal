import streamlit as st
import streamlit.components.v1 as components

components.html("""
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>CryptoGal</title>

    <!-- 
    - favicon
  -->
    <link rel="shortcut icon" href="./favicon.png" type="image/svg+xml" />

    <!-- 
    - custom css link
  -->
    <link rel="stylesheet" href="./assets/css/style.css" />

    <!-- 
    - google font link
  -->
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
      href="https://fonts.googleapis.com/css2?family=Mulish:wght@600;700;900&family=Quicksand:wght@400;500;600;700&display=swap"
      rel="stylesheet"
    />
  </head>

  <body>
    <!-- 
    - HEADER
  -->

    <header class="header" data-header>
      <div class="container">
        <a href="#" class="logo">
          <img src="./assets/images/Logo.png" alt="CryptoGal logo" />
        </a>

        <button class="menu-toggle-btn" data-nav-toggle-btn>
          <ion-icon name="menu-outline"></ion-icon>
        </button>

        <nav class="navbar">
          <ul class="navbar-list">
            <li>
              <a href="#hero" class="navbar-link">Home</a>
            </li>

            <li>
              <a href="#features" class="navbar-link">Features</a>
            </li>

            <li>
              <a href="#blog" class="navbar-link">Blog</a>
            </li>

            <li>
              <a href="#contact" class="navbar-link">Contact Us</a>
            </li>
          </ul>

          <div class="header-actions">
            <a href="#" class="header-action-link">Log in</a>

            <a href="#" class="header-action-link">Register</a>
          </div>
        </nav>
      </div>
    </header>

    <main>
      <article>
        <!-- 
        - HERO
      -->

        <section class="hero" id="hero">
          <div class="container">
            <div class="hero-content">
              <h1 class="h1 hero-title">Lets get more women into crypto</h1>

              <p class="hero-text">
                Educating young women about cryptocurrency.
              </p>

              <p class="form-text">
                <span>👩🏾‍💻</span> Sign in and kickstart you career today.
              </p>

              <form action="" class="hero-form">
                <input
                  type="email"
                  name="email"
                  required
                  placeholder="Enter Your Email"
                  class="email-field"
                />

                <button type="submit" class="btn btn-primary">
                  Get Started
                </button>
              </form>
            </div>

            <figure class="hero-banner">
              <img src="./assets/images/hero-banner.png" alt="Hero image" />
            </figure>
          </div>
        </section>

        <!-- 
        - ABOUT
      -->

        <section class="about">
          <div class="container">
            <div class="about-content">
              <div class="about-icon">
                <ion-icon name="cube"></ion-icon>
              </div>

              <h2 class="h2 about-title">Why Choose Us ?</h2>

              <p class="about-text">
                We help women succeed in crypto by promoting financial literacy,
                providing up-to-date information, and finding positive role
                models.
              </p>

              <button class="btn btn-outline">Learn More</button>
            </div>

            <ul class="about-list">
              <li>
                <div class="about-card">
                  <div class="card-icon">
                    <ion-icon name="thumbs-up"></ion-icon>
                  </div>

                  <h3 class="h3 card-title">Compare Companies</h3>

                  <p class="card-text">
                    Compare fundamentals of different companies.
                  </p>
                </div>
              </li>

              <li>
                <div class="about-card">
                  <div class="card-icon">
                    <ion-icon name="trending-up"></ion-icon>
                  </div>

                  <h3 class="h3 card-title">Crypto Tracker</h3>

                  <p class="card-text">
                    Keep track of different cryptocurrency markets.
                  </p>
                </div>
              </li>

              <li>
                <div class="about-card">
                  <div class="card-icon">
                    <ion-icon name="shield-checkmark"></ion-icon>
                  </div>

                  <h3 class="h3 card-title">Women in Crypto</h3>

                  <p class="card-text">
                    Learn and connect with impactful women in crypto.
                  </p>
                </div>
              </li>

              <li>
                <div class="about-card">
                  <div class="card-icon">
                    <ion-icon name="server"></ion-icon>
                  </div>

                  <h3 class="h3 card-title">Reports</h3>

                  <p class="card-text">
                    Review the latest information in reports.
                  </p>
                </div>
              </li>
            </ul>
          </div>
        </section>

        <!-- 
        - FEATURES
      -->

        <section class="features" id="features">
          <div class="container">
            <h2 class="h2 section-title">Awesome Features</h2>

            <p class="section-text">
              Analyze market rates for crypto, learn and connect with impactful
              women, and review reports.
            </p>

            <div class="features-wrapper">
              <figure class="features-banner">
                <img
                  src="./assets/images/features-img-1.png"
                  alt="illustration art"
                />
              </figure>

              <div class="features-content">
                <p class="features-content-subtitle">
                  <ion-icon name="sparkles"></ion-icon>

                  <span>CREATIVE FEATURES</span>
                </p>

                <h3 class="features-content-title">
                  Build
                  <strong>community</strong> with our suite of
                  <strong>resources.</strong>
                </h3>

                <p class="features-content-text">
                  We offer a suite of real-time analytics and resources to
                  empower and build the female crypto community.
                </p>

                <ul class="features-list">
                  <li class="features-list-item">
                    <ion-icon name="layers-outline"></ion-icon>

                    <p>Build your knowledge and network.</p>
                  </li>

                  <li class="features-list-item">
                    <ion-icon name="megaphone-outline"></ion-icon>

                    <p>Share insights and report findings.</p>
                  </li>
                </ul>

                <div class="btn-group">
                  <button class="btn btn-primary">Read More</button>

                  <button class="btn btn-secondary">Start Now</button>
                </div>
              </div>
            </div>

            <div class="features-wrapper">
              <figure class="features-banner">
                <img
                  src="./assets/images/features-img-2.png"
                  alt="illustration art"
                />
              </figure>

              <div class="features-content">
                <p class="features-content-subtitle">
                  <ion-icon name="sparkles"></ion-icon>

                  <span>CREATIVE FEATURES</span>
                </p>

                <h3 class="features-content-title">
                  We do the work you <strong>stay focused</strong> on
                  <strong>growing.</strong>
                </h3>

                <p class="features-content-text">
                  Our platform easily provides valuable information and
                  statisistics for you to use and learn from, allowing effective
                  growth in the crypto industry.
                </p>

                <ul class="features-list">
                  <li class="features-list-item">
                    <ion-icon name="rocket-outline"></ion-icon>

                    <p>Confidently launch your career.</p>
                  </li>

                  <li class="features-list-item">
                    <ion-icon name="wifi-outline"></ion-icon>

                    <p>Make informed decisions with newfound knowledge.</p>
                  </li>
                </ul>

                <div class="btn-group">
                  <button class="btn btn-primary">Read More</button>

                  <button class="btn btn-secondary">Start Now</button>
                </div>
              </div>
            </div>
          </div>
        </section>

        <!-- 
        - BLOG
      -->

        <section class="blog" id="blog">
          <div class="container">
            <h2 class="h2 section-title">Latest News</h2>

            <p class="section-text">
              View the latest news about all things women in crypto!
            </p>

            <ul class="blog-list">
              <li>
                <div class="blog-card">
                  <figure class="blog-banner">
                    <img src="./assets/images/art.jpg" alt="art" />
                  </figure>

                  <div class="blog-meta">
                    <span>
                      <ion-icon name="calendar-outline"></ion-icon>

                      <time datetime="2022-05-27">may 27 2022</time>
                    </span>

                    <span>
                      <ion-icon name="person-outline"></ion-icon>

                      <p>CNBCTV18.com</p>
                    </span>
                  </div>

                  <h3 class="blog-title">
                    WEF 2022: Why Web3 needs more women in spearheading
                    positions
                  </h3>

                  <p class="blog-text">
                    Today, there are several companies and non-profit
                    organizations in the crypto space that are headed by women.
                    This wave of inclusiveness is beginning to pick up steam,
                    and the timing couldn't get any better.
                  </p>

                  <a
                    href="https://www.cnbctv18.com/cryptocurrency/wef-2022-why-web3-needs-more-women-in-spearheading-positions-13638632.htm"
                    class="blog-link-btn"
                  >
                    <span>Learn More</span>

                    <ion-icon name="chevron-forward-outline"></ion-icon>
                  </a>
                </div>
              </li>

              <li>
                <div class="blog-card">
                  <figure class="blog-banner">
                    <img src="./assets/images/visual.jpg" alt="visual" />
                  </figure>

                  <div class="blog-meta">
                    <span>
                      <ion-icon name="calendar-outline"></ion-icon>

                      <time datetime="2021-05-30">may 30 2021</time>
                    </span>

                    <span>
                      <ion-icon name="person-outline"></ion-icon>

                      <p>Emily Guy Birken</p>
                    </span>
                  </div>

                  <h3 class="blog-title">Why Women Are Better Investors</h3>

                  <p class="blog-text">
                    Understanding how women invest and why they excel can help
                    everyone, regardless of gender, do a better job with their
                    investments.
                  </p>

                  <a
                    href="https://www.forbes.com/advisor/investing/woman-better-investors/"
                    class="blog-link-btn"
                  >
                    <span>Learn More</span>

                    <ion-icon name="chevron-forward-outline"></ion-icon>
                  </a>
                </div>
              </li>

              <li>
                <div class="blog-card">
                  <figure class="blog-banner">
                    <img src="./assets/images/bitcoin.jpg" alt="bitcoin" />
                  </figure>

                  <div class="blog-meta">
                    <span>
                      <ion-icon name="calendar-outline"></ion-icon>

                      <time datetime="2021-11-17">November 17 2021</time>
                    </span>

                    <span>
                      <ion-icon name="person-outline"></ion-icon>

                      <p>April Miller</p>
                    </span>
                  </div>

                  <h3 class="blog-title">
                    Environmentally Friendly Cryptocurrency: 5 Leading Cryptos
                    and 3 Ways Others Can Follow Suit
                  </h3>

                  <p class="blog-text">
                    The complex world of cryptocurrency is unsustainable, but
                    some crypto firms are trying to change that. Thankfully,
                    environmentally friendly cryptocurrency is on the rise.
                    Companies including Cardano and Chia are helping the
                    industry achieve sustainability.
                  </p>

                  <a
                    href="https://earth.org/environmentally-friendly-cryptocurrency/"
                    class="blog-link-btn"
                  >
                    <span>Learn More</span>

                    <ion-icon name="chevron-forward-outline"></ion-icon>
                  </a>
                </div>
              </li>
            </ul>
          </div>
        </section>

        <!-- 
      - CONTACT
    -->

        <section class="contact" id="contact">
          <div class="container">
            <h2 class="h2 section-title">Contact Us</h2>

            <p class="section-text">
              Any questions? Want to learn more about CryptoGal? Send us a
              message here!
            </p>

            <div class="contact-wrapper">
              <form action="" class="contact-form">
                <div class="wrapper-flex">
                  <div class="input-wrapper">
                    <label for="name">Name*</label>

                    <input
                      type="text"
                      name="name"
                      id="name"
                      required
                      placeholder="Enter Your Name"
                      class="input-field"
                    />
                  </div>

                  <div class="input-wrapper">
                    <label for="emai">Email*</label>

                    <input
                      type="text"
                      name="email"
                      id="email"
                      required
                      placeholder="Enter Your Email"
                      class="input-field"
                    />
                  </div>
                </div>

                <label for="message">Message*</label>

                <textarea
                  name="message"
                  id="message"
                  required
                  placeholder="Type Your Message"
                  class="input-field"
                ></textarea>

                <button
                  style="background-color: 5a4fdc;"
                  ;
                  type="submit"
                  class="btn btn-primary"
                >
                  <span>Send Message</span>

                  <ion-icon name="paper-plane-outline"></ion-icon>
                </button>
              </form>

              <ul class="contact-list">
                <li>
                  <a href="mailto:support@website.com" class="contact-link">
                    <ion-icon name="mail-outline"></ion-icon>

                    <span>: support@cryptogal.com</span>
                  </a>
                </li>

                <li>
                  <a href="#" class="contact-link">
                    <ion-icon name="globe-outline"></ion-icon>

                    <span>: www.cryptogal.com</span>
                  </a>
                </li>

                <li>
                  <a href="tel:+0011234567890" class="contact-link">
                    <ion-icon name="call-outline"></ion-icon>

                    <span>: (+001) 501 766 0989</span>
                  </a>
                </li>

                <li>
                  <div class="contact-link">
                    <ion-icon name="time-outline"></ion-icon>

                    <span>: 9:00 AM - 6:00 PM</span>
                  </div>
                </li>

                <li>
                  <a href="#" class="contact-link">
                    <ion-icon name="location-outline"></ion-icon>

                    <address>
                      : 1689 Ridge Drive Rochelle Park, CA 95070
                    </address>
                  </a>
                </li>
              </ul>
            </div>
          </div>
        </section>
      </article>
    </main>

    <!-- 
    - FOOTER
  -->

    <footer>
      <div style="background-color: #5a4fdc;" class="footer-top">
        <div class="container">
          <div class="footer-brand">
            <a href="#" class="logo">
              <img src="./assets/images/LogoWhite.png" alt="CryptoGal logo" />
            </a>

            <p class="footer-text">
              CyrptoGal works to help women succeed in crypto by promoting
              financial literacy, providing up-to-date information, and finding
              positive role models.
            </p>

            <ul class="social-list">
              <li>
                <a href="#" class="social-link">
                  <ion-icon name="logo-facebook"></ion-icon>
                </a>
              </li>

              <li>
                <a href="#" class="social-link">
                  <ion-icon name="logo-twitter"></ion-icon>
                </a>
              </li>

              <li>
                <a href="#" class="social-link">
                  <ion-icon name="logo-instagram"></ion-icon>
                </a>
              </li>

              <li>
                <a href="#" class="social-link">
                  <ion-icon name="logo-linkedin"></ion-icon>
                </a>
              </li>
            </ul>
          </div>

          <div class="footer-link-box">
            <ul class="footer-list">
              <li>
                <p class="footer-item-title">ABOUT US</p>
              </li>

              <li>
                <a href="#" class="footer-link">Works</a>
              </li>

              <li>
                <a href="#" class="footer-link">Strategy</a>
              </li>

              <li>
                <a href="#" class="footer-link">Releases</a>
              </li>

              <li>
                <a href="#" class="footer-link">Press</a>
              </li>

              <li>
                <a href="#" class="footer-link">Mission</a>
              </li>
            </ul>

            <ul class="footer-list">
              <li>
                <p class="footer-item-title">CUSTOMERS</p>
              </li>

              <li>
                <a href="#" class="footer-link">Tranding</a>
              </li>

              <li>
                <a href="#" class="footer-link">Popular</a>
              </li>

              <li>
                <a href="#" class="footer-link">Customers</a>
              </li>

              <li>
                <a href="#" class="footer-link">Features</a>
              </li>
            </ul>

            <ul class="footer-list">
              <li>
                <p class="footer-item-title">SUPPORT</p>
              </li>

              <li>
                <a href="#" class="footer-link">Developers</a>
              </li>

              <li>
                <a href="#" class="footer-link">Support</a>
              </li>

              <li>
                <a href="#" class="footer-link">Customer Service</a>
              </li>

              <li>
                <a href="#" class="footer-link">Get Started</a>
              </li>

              <li>
                <a href="#" class="footer-link">Guide</a>
              </li>
            </ul>
          </div>
        </div>
      </div>

      <div style="background-color: #5a4fdc;" class="footer-bottom">
        <div class="container">
          <p class="copyright">
            &copy; 2022 <a href="">CryptoGal</a>. All Right Reserved
          </p>
        </div>
      </div>
    </footer>

    <!-- 
  - custom js link
-->
    <script src="./assets/js/script.js"></script>

    <!-- 
  - ionicon link
-->
    <script
      type="module"
      src="https://unpkg.com/ionicons@5.5.2/dist/ionicons/ionicons.esm.js"
    ></script>
    <script
      nomodule
      src="https://unpkg.com/ionicons@5.5.2/dist/ionicons/ionicons.js"
    ></script>
  </body>
</html>
""", height=600)
