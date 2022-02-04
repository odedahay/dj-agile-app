(function () {
    const navbar = document.querySelector('#navbarSideCollapse');
    const offcanvas = document.querySelector('.offcanvas-collapse');
    const iconMenu = document.querySelector('#iconMenu'); 

    navbar.addEventListener('click', function () {
        offcanvas.classList.toggle('open');

        if(iconMenu.classList.contains('bi-filter-right')){
            iconMenu.classList.remove('bi-filter-right');
            iconMenu.classList.add('bi-filter-left');
        }else{
            iconMenu.classList.remove('bi-filter-left');
            iconMenu.classList.add('bi-filter-right');
        }
    });


    // Stickey header
    // const throttle = (func, delay) => {
    //   last = 0;

    //   return( ...args ) =>{
    //     const now = new Date().getTime();
    //     if(now - last < delay ){
    //       return;
    //     }else{
    //       last = now;
    //       return func(...args);
    //     }
    //   }
    // }


  const throttle = (func, limit) => {
    let lastFunc;
    let lastRan;
    
    return function() {
      const context = this;
      const args = arguments;
      if (!lastRan) {
        func.apply(context, args)
        lastRan = Date.now();
      } else {
        clearTimeout(lastFunc);
        lastFunc = setTimeout(function() {
            if ((Date.now() - lastRan) >= limit) {
              func.apply(context, args);
              lastRan = Date.now();
            }
        }, limit - (Date.now() - lastRan));
      }
    }
  }

    siteHeader = document.querySelector(".sec-navigation");
    let previousScrollY = window.scrollY
    // const scrollDirection;

    window.addEventListener("scroll", throttle( ()=> runOnScroll(), 200)) ;

    function runOnScroll(){
      //determineScrollDirection();

      if(window.scrollY > 80){
        siteHeader.classList.add('sec-navigation__screen');
      }else{
        siteHeader.classList.remove('sec-navigation__screen');
      }
    }
    
    function determineScrollDirection(){
      if(window.scrollY > previousScrollY){
        scrollDirection = 'down';
      }else{
        scrollDirection = 'up'
      }
      previousScrollY =  window.scrollY;
    }

})()

function readMoreButton() {
    var moreText = document.getElementById("more");
    var btnText = document.getElementById("myBtn");
  
    if (btnText.innerHTML == 'Read more <i class="bi bi-chevron-down"></i>') {
      btnText.innerHTML = 'Read less <i class="bi bi-chevron-up"></i>'; 
      // moreText.classList.remove('hide-content');
      // moreText.classList.add('show-content');
      moreText.classList.toggle('open')
     
    } 
    else {
  
      btnText.innerHTML = 'Read more <i class="bi bi-chevron-down"></i>'; 
      // moreText.classList.remove('show-content');
      // moreText.classList.add('hide-content');
      moreText.classList.remove('open');
    }
  }