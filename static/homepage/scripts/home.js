/*property

*/


const Home = (function() {
  "use strict";

  /*------------------------------------------------------------------------
   *              CONSTANTS
   */

   const ANIMATION_DURATION = 1000 ;
   const BLACK_COVER_CLASS = 'blackCover'
   const DIV_SLIDE_ID = 'slide';
   const IMAGE_DIV_SLIDE_ID = 'imgDiv';
   const LAST_SLIDE_ID = 'slide6';
   const SLIDE_CLASS = 'slide';

  /*------------------------------------------------------------------------
   *              PRIVATE VARIABLES
   */
  let isInitialFade = true;
  let lastWindowHeight = 0;
  let lastWindowWidth = 0;
  let numOfSlides = 0;
  let slides = [];

  /*------------------------------------------------------------------------
   *              PRIVATE METHOD DECLARATIONS
   */

  let fadeInImages;
  let fadeImage;
  let fadeSlide;
  let fadeSlide1;
  let hoverOn;
  let hoverOff;
  let init;
  let scrollToDiv;
  let setScrollAnimations;
  let setScrollHeights;



  /*------------------------------------------------------------------------
   *              PRIVATE METHOD DECLARATIONS
   */

  fadeInImages = function(){
    let numOfSlides = document.getElementsByClassName(SLIDE_CLASS).length
    for(let i=1; i<=numOfSlides; i++){
        fadeImage(IMAGE_DIV_SLIDE_ID + i)
    }
      setTimeout(function(){setScrollAnimations()},ANIMATION_DURATION)

  };

  fadeImage = function(slideid){
    let slide = document.getElementById(slideid)
    $(slide).animate({opacity: 1}, ANIMATION_DURATION)
  }

  fadeSlide = function(slideNum, isFadeIn=true, duration=ANIMATION_DURATION){
    let slide = document.getElementById(DIV_SLIDE_ID + 'div' + slideNum)
    let black = document.getElementsByClassName(BLACK_COVER_CLASS)[slideNum-1]

    if (isFadeIn){
      if ($(slide).css('opacity') === "0") {
          if (slideNum === 1 && isInitialFade){
             $(slide).css('opacity',1)
             fadeSlide1()
             return
          }
          else{
            //console.log("FADING IN: " + slideNum) 
            $(slide).animate({opacity: 1}, duration)
            $(black).animate({opacity:.6},duration/2)
          }
      }
    }
    else{
      if ($(slide).css('opacity') === "1") {
        // console.log("FADING OUT: " + slideNum) 
          $(slide).animate({opacity: 0}, duration)
          $(black).animate({opacity:.4},duration/2)
      }
    }
  };

  fadeSlide1 = function(){
    let we = document.getElementById("we")
    let are = document.getElementById("are")
    let rt = document.getElementById("rifftide")
    let da = document.getElementById("down1")
    $(we).animate({opacity: 1}, ANIMATION_DURATION)
    setTimeout(function(){$(are).animate({opacity: 1}, 800)},600)
    setTimeout(function(){$(rt).animate({opacity: 1}, 800)},1200)
    setTimeout(function(){$(da).animate({opacity: 1}, 800)},2400)
    isInitialFade = false
  }

  init = function(onInitializedCallback) {
      console.log("Started init...");
      fadeInImages()
      setTimeout(function() {window.onscroll = function() {setScrollAnimations()}},1500);
  };

  scrollToDiv = function(divId){
    let newDiv = document.getElementById(divId)
    let screenHeight = window.innerHeight;
    let divHeight = newDiv.clientHeight;
    let scrollPos = ($(newDiv).offset().top - ((screenHeight+ 55) - divHeight)/2);
    if (divId === LAST_SLIDE_ID){
      scrollPos = document.body.offsetHeight - divHeight
    }
    $('html, body').animate({
      scrollTop: scrollPos
    }, 600, function(){});
  }

  setScrollAnimations = function(){

    if(window.innerWidth != lastWindowWidth || window.innerHeight != lastWindowHeight){
      lastWindowHeight = window.innerHeight;
      lastWindowWidth = window.innerWidth;

      setScrollHeights()
    }
    
    let scrollTop = document.documentElement.scrollTop;

    if ((window.innerHeight + window.pageYOffset) >= document.body.offsetHeight) {
        fadeSlide((6), true)
    }

    for(let i=0; i<numOfSlides; i++){
        // //Fade In
        if (scrollTop >= slides[i].ScrollInHeight && scrollTop < slides[i].ScrollOutHeight) {
            fadeSlide((i+1), true)
            fadeSlide((i + 2),false,200)
        }
        // //fade Out
        else if (scrollTop > slides[i].ScrollOutHeight) {
          fadeSlide((i+1), false, 200)
        }
    }

  };

  setScrollHeights = function(){
    numOfSlides = document.getElementsByClassName(SLIDE_CLASS).length
    let screenHeight = window.innerHeight;
  
    for(let i=1; i<=numOfSlides; i++){
        let divI = document.getElementById(DIV_SLIDE_ID + i)
        let inh = ($(divI).offset().top - ((screenHeight+ 55) - divI.clientHeight)/2)
        if (i==0){
          inh=0;
        }
        if(i==numOfSlides){}
        if(i+1 == numOfSlides){

        }
        let div = {div: divI,
           divHeight: divI.clientHeight,
            ScrollInHeight: inh - 5,
             ScrollOutHeight:inh + (divI.clientHeight/2)}
        slides.push(div)
        }
  }

  /*------------------------------------------------------------------------
   *              PUBLIC METHODS
   */
  return {
      init,
      hoverOn,
      hoverOff,
      scrollToDiv,
  };
}());
