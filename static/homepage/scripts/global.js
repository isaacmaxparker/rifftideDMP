/*property

*/


const Global = (function() {
    "use strict";
  
    /*------------------------------------------------------------------------
     *              CONSTANTS
     */
  
    /*------------------------------------------------------------------------
     *              PRIVATE VARIABLES
     */
  
    /*------------------------------------------------------------------------
     *              PRIVATE METHOD DECLARATIONS
     */

    let hoverOn;
    let hoverOff;
    let init;  
    let scrollToDiv;
    /*------------------------------------------------------------------------
     *              PRIVATE METHOD DECLARATIONS
     */
  
    hoverOn = function(id){
      $(document.getElementById(id)).animate({opacity:.7},50)
    }
    hoverOff = function(id){
      $(document.getElementById(id)).animate({opacity:1},50)
    }
  
    init = function(onInitializedCallback) {
        console.log("Started global init...");
        window.scrollTo(0,0)
    };

    scrollToDiv = function(divId, speed=600){
      let newDiv = document.getElementById(divId)
      let screenHeight = window.innerHeight;
      let divHeight = newDiv.clientHeight;
      let scrollPos = ($(newDiv).offset().top - ((screenHeight+ 55) - divHeight)/2);
      $('html, body').animate({
        scrollTop: scrollPos
      }, speed, function(){});
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
  