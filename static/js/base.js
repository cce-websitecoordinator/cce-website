window.addEventListener("load", function () {
  const topbar = document.querySelector(".topbar");
  const navbar = document.querySelector(".navbar");
  const navbarHeight = navbar.getBoundingClientRect().height;



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


{
  window.onload= () => {
   document.getElementById('loader').style.display = 'none';
    console.log('loaded');
    let homeArrow = document.getElementById("home--arrow")
    if(homeArrow){
      homeArrow.classList.remove("hidden")
      homeArrow.classList.add("flex")
    }
  }
  
}