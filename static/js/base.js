window.addEventListener("load", function () {
  const topbar = document.querySelector(".topbar");
  const navbar = document.querySelector(".navbar");
  const navbarHeight = navbar.getBoundingClientRect().height;
  const searchButton = document.getElementById("search_button"),
    searchContainer = document.getElementById("search_container"),
    navlinks = document.getElementById("navlinks");

  //Dropdown menu for the navbar

  // Down-aarow Animation
  document
    .getElementById("dropdownBtn")
    .addEventListener("mouseenter", function () {
      console.log("Clicked");
      document.getElementById("bounce").classList.add("animate-bounce");
      document.getElementById("bounce").classList.add("text-[#007FFF]");
    });
  document
    .getElementById("dropdownBtn")
    .addEventListener("mouseleave", function () {
      console.log("Clicked");
      document.getElementById("bounce").classList.remove("animate-bounce");
      document.getElementById("bounce").classList.remove("text-[#007FFF]");
    });

  //Dropdown menu
  document.getElementById("dropdownBtn").addEventListener("click", function () {
    console.log("Clicked");
    document.getElementById("dropdown").classList.toggle("show");
  });
  document.getElementById("dropdown").addEventListener("mouseleave", () => {
    document.getElementById("dropdown").classList.remove("show");
  });
  // Search Button
  searchContainer.addEventListener("mouseenter", function () {
    navlinks.classList.add("hidden");
    searchContainer.classList.add("bg-white");
    searchContainer.classList.add("search-shadow");
  });
  searchContainer.addEventListener("mouseleave", function () {
    searchContainer.classList.remove("bg-white");
    setTimeout(() => {
      navlinks.classList.remove("hidden");
      searchContainer.classList.remove("search-shadow");
      document.activeElement.blur();
    }, 500);
  });

  // Navbar Scrolling

  window.addEventListener("scroll", function () {
    if (window.scrollY > navbarHeight) {
      navbar.classList.add("fixed-nav");
    } else {
      navbar.classList.remove("fixed-nav");
      if (topbar) {
        navbar.style.top = topbar.getBoundingClientRect().height + 20 + "px";
      }
    }
  });
});

// scroll to top button
document.getElementById("scroll-to-top").addEventListener("click", function () {
  window.scrollTo({
    top: 0,
    left: 0,
    behavior: "smooth",
  });
});


