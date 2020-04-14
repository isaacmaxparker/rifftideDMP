/*property

*/


const About = (function() {
    "use strict";
  
    /*------------------------------------------------------------------------
     *              CONSTANTS
     */
    const ALL_PROFILES_ID = 'memberProfiles';
    const ANIMATION_DURATION = 1000 ;
    const ANIMATION_DURATION_SHORT = 100 ;
    const GROUP_BIO_IMAGE_DIV = "imgDiv";
    const GROUP_BIO_TEXT_DIV = "groupBioText";
    const GROUP_BIO_DIV = "groupBioDiv";
    const GROUP_DIV_ID = 'pastGroup';
    const MEMBER_PROFILE_ID = 'memberProfile';
    const NUM_OF_PROFILES = 3;
    const NUM_OF_GROUPS = 6;
    const NUM_OF_TITLES = 3;
    const OUR_STORY_TITLE = 'ourStoryTitle';
    const OUR_STORY_BODY = 'ourStoryBody';
    const PREVIOUS_MEMBERS_TITLE = 'pastGroupsTitle';
  
    /*------------------------------------------------------------------------
     *              PRIVATE VARIABLES
     */
    let lastWindowHeight = 0;
    let lastWindowWidth = 0;
    let profiles = [];
    let groups = [];
    let titles = [];
  
    /*------------------------------------------------------------------------
     *              PRIVATE METHOD DECLARATIONS
     */

    let animateProfile;
    let animateGroup;
    let animateTitle;
    let fadein;
    let init;
    let setScrollAnimations;
    let setScrollHeights;
  
  
    /*------------------------------------------------------------------------
     *              PRIVATE METHOD DECLARATIONS
     */

    animateProfile = function(profileNum, percentage, isAnimateIn){
      let div = document.getElementById(MEMBER_PROFILE_ID + profileNum)
      if (isAnimateIn){
        //$(div).css('opacity',position)
        if (percentage < .09){
          $(div.children[0].children[0]).css({'width':`18vw`,'opacity':`.1`,'filter':`grayscale(100%)`})
          $(div.children[1].children[0]).css({'opacity':`0`,'filter':`grayscale(100%)`})
          $(div.children[1].children[1]).css({'opacity':`0`})
          $(div.children[2]).css({'transform':`rotate(29deg)`,'left':`20%`})
        }
        else{
          $(div.children[0].children[0]).css({'width':`${18 + (2*percentage)}vw`,'opacity':`${.1 + (.9 * percentage)}`,'filter':`grayscale(${100 - (100 * percentage)}%)`})
          $(div.children[1].children[0]).css({'opacity':`${0 + (percentage)}`,'filter':`grayscale(${100 - (100 * percentage)}%)`})
          $(div.children[1].children[1]).css({'opacity':`${0 + (percentage)}`})
          $(div.children[2]).css({'transform':`rotate(${29 - (29*percentage)}deg)`,'left':`${20 - (20*percentage)}%`})
        }
  
      }
      else{
        if(percentage !== 1){
          $(div.children[0].children[0]).css({'width':`${20 - (2*percentage)}vw`,'opacity':`${1 - (.9*percentage)}`,'filter':`grayscale(${0 + (100 * percentage)}%)`})
        }
        $(div.children[1].children[0]).css({'opacity':`${1 - (percentage)}`,'filter':`grayscale(${0 + (100 * percentage)}%)`})
        $(div.children[1].children[1]).css({'opacity':`${1 - (percentage)}`})
        $(div.children[2]).css({'transform':`rotate(${(29*percentage)}deg)`,'left':`${(20*percentage)}%`})
      }
    }

    animateGroup = function(profileNum, percentage, isAnimateIn){
      let div = document.getElementById(GROUP_DIV_ID + profileNum)
      if (isAnimateIn){
        //$(div).css('opacity',position)       
        
        if (percentage < .09){
          $(div.children[0].children[0]).css({'left':`-65vw`}) 
          $(div.children[1]).css({'opacity':`0`})
        }
        else{
        $(div.children[0].children[0]).css({'left':`${((-65 * (1-percentage) + 9))}vw`}) 
        $(div.children[1]).css({'opacity':`${1*percentage}`})
        }
      }
      else{
        $(div.children[0].children[0]).css({'left':`${((-65 * percentage) + 9)}vw`})
        $(div.children[1]).css({'opacity':`${1-percentage}`})
      }
    }

    animateTitle = function(id, percentage){
      let div = document.getElementById(id)
      if (percentage < .082){
        $(div).css('opacity',0)
      }
      else{
      $(div).css({'opacity':`${percentage}`})
      }
    }

    fadein = function(){
        $(document.getElementById(GROUP_BIO_IMAGE_DIV)).animate({opacity:1},ANIMATION_DURATION)
        $(document.getElementById(GROUP_BIO_TEXT_DIV)).animate({opacity:1},ANIMATION_DURATION)
    }
  
    init = function(onInitializedCallback) {
        fadein()
        window.onscroll = function() {setScrollAnimations()}
        setScrollAnimations()
    };

    setScrollAnimations = function(){
      if(window.innerWidth != lastWindowWidth || window.innerHeight != lastWindowHeight){
        lastWindowHeight = window.innerHeight;
        lastWindowWidth = window.innerWidth;
  
        setScrollHeights()
      }

      let scrollTop = document.documentElement.scrollTop;
  
      for(let i=0; i<NUM_OF_PROFILES; i++){
        // //Fade In
        if (scrollTop >= profiles[i].scrollInStart && scrollTop < profiles[i].scrollInStop) {
          let dist = profiles[i].scrollInStop - profiles[i].scrollInStart
          let pos = ((scrollTop - profiles[i].scrollInStart) / dist)
          animateProfile((i+1),pos,true)
          if (i != 0){
            animateProfile(i,1,false)
          }
          if (i != NUM_OF_PROFILES -1){
            animateProfile(i+2,1,false)
          } 
          return
        }
        // //fade Out
        else if (scrollTop > profiles[i].scrollOutStart && scrollTop < profiles[i].scrollOutStop) {
          let dist = profiles[i].scrollOutStop - profiles[i].scrollOutStart
          let pos = ((scrollTop - profiles[i].scrollOutStart) / dist)
          animateProfile((i+1),pos,false)
          return
        }
      }
      for(let i=0; i<NUM_OF_GROUPS; i++){
      // //Fade In
          if (scrollTop >= groups[i].scrollInStart && scrollTop < groups[i].scrollInStop) {
            let dist = groups[i].scrollInStop - groups[i].scrollInStart
            let pos = ((scrollTop - groups[i].scrollInStart) / dist)
            animateGroup((i+1),pos,true)
            if (i != 0){
              animateGroup(i,1,false)
            }
            if (i != NUM_OF_GROUPS -1){
              animateGroup(i+2,1,false)
            } 
            else{
              animateGroup(1,1,false)
            }
            return
          }
          // //fade Out
          else if (scrollTop > groups[i].scrollOutStart && scrollTop < groups[i].scrollOutStop) {
            let dist = groups[i].scrollOutStop - groups[i].scrollOutStart
            let pos = ((scrollTop - groups[i].scrollOutStart) / dist)
            animateGroup((i+1),pos,false)
            return
          }
      }
      for(let i=0; i<NUM_OF_TITLES; i++){
        //Fade In
            if (scrollTop >= titles[i].scrollInStart && scrollTop < titles[i].scrollInStop) {
              let dist = titles[i].scrollInStop - titles[i].scrollInStart
              let pos = ((scrollTop - titles[i].scrollInStart) / dist)
              animateTitle(titles[i].divID,pos)
              return
            }
            else if (scrollTop > titles[i].divTop && scrollTop < titles[i].divBottom){
              animateTitle(titles[i].divID,1)
            }
        }
 
      


    }

    setScrollHeights = function(){
      profiles = []
      groups = []
      titles = []
      let screenHeight = window.innerHeight;
      for(let i=1; i<=NUM_OF_PROFILES; i++){
          let profile = document.getElementById(MEMBER_PROFILE_ID + i)
          let profTop = ($(profile).offset().top - (screenHeight/2))
          let slideHeight = profile.clientHeight;
          let div = {
            scrollInStart: profTop,
            scrollInStop: profTop + (slideHeight/3),
            scrollOutStart: profTop + (slideHeight/2),
            scrollOutStop:profTop + slideHeight,
          }
          profiles.push(div)
      }
        
        
      for(let i=1; i<=NUM_OF_GROUPS; i++){
        let profile = document.getElementById(GROUP_DIV_ID + i)
        let profTop = ($(profile).offset().top - (screenHeight/2))
        let slideHeight = profile.clientHeight;
        let div = {
          scrollInStart: profTop,
          scrollInStop: profTop + (slideHeight/3),
          scrollOutStart: profTop + (slideHeight/2),
          scrollOutStop:profTop + slideHeight,
        }
        groups.push(div)
      }

      let prevTitle = document.getElementById(PREVIOUS_MEMBERS_TITLE);
      let titleTop = $(prevTitle).offset().top;
      let titleDiv = {
        scrollInStart:titleTop - (screenHeight /2),
        scrollInStop: titleTop - (screenHeight /2) + screenHeight/6,
        divTop:titleTop,
        divBottom:titleTop + prevTitle.clientHeight,
        divID: PREVIOUS_MEMBERS_TITLE,
      }
      titles.push(titleDiv)
      let storyTitle = document.getElementById(OUR_STORY_TITLE);
      let storyTop = $(storyTitle).offset().top;
      let storyTitleDiv = {
        scrollInStart: storyTop - (screenHeight /2),
        scrollInStop: storyTop - (screenHeight/2) + screenHeight/6,
        divTop:storyTop,
        divBottom:storyTop + storyTitle.clientHeight,
        divID: OUR_STORY_TITLE,
      }
      titles.push(storyTitleDiv)
      let storyBody = document.getElementById(OUR_STORY_BODY);
      let storyBodTop = $(storyBody).offset().top;
      let storyBodyDiv = {
        scrollInStart: storyBodTop - (screenHeight /2),
        scrollInStop: storyBodTop - (screenHeight/2) + screenHeight/6,
        divTop:storyBodTop,
        divBottom:storyBodTop + storyBody.clientHeight,
        divID: OUR_STORY_BODY,
      }
      titles.push(storyBodyDiv)

    }



    /*------------------------------------------------------------------------
     *              PUBLIC METHODS
     */
    return {
        init,
    };
  }());
  