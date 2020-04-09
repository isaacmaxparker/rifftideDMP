/*property

*/


const Cards = (function() {
    "use strict";
  
    /*------------------------------------------------------------------------
     *              CONSTANTS
     */

    const ANIMATION_DURATION = 3000;
    const ANIMATION_DURATION_MEDIUM = 750;
    const ANIMATION_DURATION_SHORT = 250;
    const ACTIVE_CARD_CLASS = 'activeCard';
    const CARDSLIST_DIV_ID = 'cardLists';
    const CARDLIST_ID = 'cardList'
    const CARDS_URL = 'https://raw.githubusercontent.com/isaacmcdgl/RifftideJSON/master/JSON/cards.json'
    const CAROUSEL_ID = 'cardsScroller';
    const CARD_CONTAINER_CLASS = 'cardContainer'
    const EVENT_INDEX = 'data-evntindex';
    const EVENTS_URL = 'https://raw.githubusercontent.com/isaacmcdgl/RifftideJSON/master/JSON/events.json'
    const FILTERS_DIV_ID = 'filtersDiv';
    const IMAGE_BASE_URL = 'Images/cards/'
    const IMAGE_FILE_TYPE = '.png'
    const INACTIVE_CLASS = 'inactiveCard';
    const LIST_SECTION_CLASS = 'listSection';
    const MEM_INDEX = 'data-memindex';
    const MEMBERS_URL = 'https://raw.githubusercontent.com/isaacmcdgl/RifftideJSON/master/JSON/members.json'
    const REQUEST_GET = "GET";
    const REQUEST_STATUS_OK = 200;
    const REQUEST_STATUS_ERROR = 400;
    const SMALL_CARD_CLASS = 'smallCard';
    const SLIDER_CARD_CLASS = 'sliderCard';
    const SLIDER_ID = 'cardSlider';
    const MODAL_ID = 'cardPopUp';

  
    /*------------------------------------------------------------------------
     *              PRIVATE VARIABLES
     */

    let items = []
    let cards = []
    let members = []
    let events =[]
    let showInactives = true;
    let cardsLoaded = false;
    let membsLoaded = false;
    let eventsLoaded = false;
    let gridContent = '';
    let popContent;
    let sortByEvent = true;
    let slider = ''
    let currIndex = 0;
    let width = 0;
    let totalWidth = 0;
  
    /*------------------------------------------------------------------------
     *              PRIVATE METHOD DECLARATIONS
     */

    let ajax;
    let addCardList;
    let addCardstoPopover;
    let closeModal;
    let htmlDiv;
    let htmlImg;
    let loadCards;
    let loadMembers;
    let init;  
    let next;
    let prev;
    let resize;
    let setInactive;
    let showInactive;
    let setUpCards
    let setUpPopover;
    let toggleFilters;
    let showCards;
    let switchCards;
    
    
    /*------------------------------------------------------------------------
     *              PUBLIC METHODS
     */

    ajax = function(url, successCallback, failureCallback, skipJsonParse) {

         let request = new XMLHttpRequest();
         request.open(REQUEST_GET, url, true);

         request.onload = function() {
             if (this.status >= REQUEST_STATUS_OK && this.status < REQUEST_STATUS_ERROR) {
                
                 let data = (
                     skipJsonParse 
                     ? request.response 
                     : JSON.parse(request.response)
                 );

                 if (typeof successCallback === 'function') {
                     successCallback(data);
                 }
             } else {
                 if (typeof failureCallback === 'function') {
                     failureCallback(request);
                 }
             }
         };

         request.onerror = failureCallback;
         request.send();
    };

    addCardList = function(cardGroup){
        let id;
        let className = LIST_SECTION_CLASS
        let contents;
        let cardsString=''
        if(sortByEvent){

            id=`cardlist__${cardGroup.eventCards[0].eventcode}`
            contents = htmlDiv(``,'listTitle',`${cardGroup.eventName}`)
               
            cardGroup.eventCards.forEach(element => {
                let attr = `data-event="${element.eventcode}" data-member="${element.member}" data-memindex="${element.memberindex}" data-evntindex="${element.eventindex}" onclick="showCards(this)"`
                cardsString += htmlImg(`${element.eventcode}_${element.member}_${element.memberindex}`,SMALL_CARD_CLASS,`${IMAGE_BASE_URL}${element.img}${IMAGE_FILE_TYPE}`,attr)
            });

        }
        else{
            id=`cardlist__${cardGroup.name}`
            contents = htmlDiv(``,'listTitle',`${cardGroup.name}`)
            cardGroup.memberCards.forEach(element => {
                let attr = `data-event="${element.eventcode}" data-member="${element.member}" data-memindex="${element.memberindex}" data-evntindex="${element.eventindex}" onclick="showCards(this)"`
                cardsString += htmlImg(`${element.eventcode}_${element.member}_${element.memberindex}`,SMALL_CARD_CLASS,`${IMAGE_BASE_URL}${element.img}${IMAGE_FILE_TYPE}`,attr)
            });
        }



        contents += htmlDiv(``,CARDLIST_ID,cardsString)
        gridContent+= htmlDiv(id, className, contents)
        gridContent+=htmlDiv('','spacer','')
    }

    addCardstoPopover = function(cardsToAdd){
        cardsToAdd.forEach(element => {
            let content;
            if(sortByEvent){
                content = htmlImg('',`${SLIDER_CARD_CLASS} ${ element.memberindex === 1 ?  ACTIVE_CARD_CLASS :''}`,`${IMAGE_BASE_URL}${element.img}${IMAGE_FILE_TYPE}`,`onClick="switchCards(${element.memberindex})"`)
            }
            else{
                content = htmlImg('',`${SLIDER_CARD_CLASS} ${ element.eventindex === 1 ?  ACTIVE_CARD_CLASS :''}`,`${IMAGE_BASE_URL}${element.img}${IMAGE_FILE_TYPE}`,`onClick="switchCards(${element.eventindex})"`)
            }
            popContent+=htmlDiv('',CARD_CONTAINER_CLASS,content)
        });
    }

    closeModal = function(){
        let modal = document.getElementById(MODAL_ID)
        $(modal).animate({'opacity':0}, ANIMATION_DURATION_SHORT)
        setTimeout(function(){$(modal).css('display','none')},ANIMATION_DURATION_SHORT)
    }

    htmlImg = function(id,className,imageSrc,extAtt){
        return `<img id="${id}" class="${className}" src="${imageSrc}" ${extAtt} /> `
    };

    htmlDiv = function(id,className,contents){
        return `<div id="${id}" class="${className}">${contents}</div>`
    }

    loadCards = function(){
        cards=[];
            ajax(CARDS_URL, function(data) {
                cards = data;
                cardsLoaded = true;
                if(sortByEvent){
                    ajax(EVENTS_URL, function(data) {
                        events = data;
                        eventsLoaded = true;
                        setUpCards()
                        //TO DO: ADD IN A LOADING THING AND TAKE IT AWAY
                    }
                );
                }
                else{
                    ajax(MEMBERS_URL, function(data) {
                        members = data;
                        membsLoaded = true;
                        setUpCards()
                        //TO DO: ADD IN A LOADING THING AND TAKE IT AWAY
                        }
                    );
                }

            //TO DO: ADD IN A LOADING THING AND TAKE IT AWAY
            }
        );
    }

    loadMembers = function(callback){
        if (membsLoaded){
            return
        }
        ajax(MEMBERS_URL, function(data) {
            members = data;
            membsLoaded = true;

            if (typeof(callback) ==='function'){
                callback()
            }
            //TO DO: ADD IN A LOADING THING AND TAKE IT AWAY
            },
        );
    }

    init = function(onInitializedCallback) {
        let carousel = document.getElementById(CAROUSEL_ID);
        loadCards()
        if(showInactive){
            loadMembers()
        }
        slider = document.getElementById(SLIDER_ID);
        items = carousel.getElementsByClassName(CARD_CONTAINER_CLASS);
        window.onresize = resize;  
       
        if(sortByEvent){
            document.getElementById('eventFilter').classList.add('activeFilter')
        }
        else{
            document.getElementById('memberFilter').classList.add('activeFilter')
        }
    };

    prev = function() {
        switchCards(--currIndex);
      }
      
    next = function() {
        switchCards(++currIndex);    
      }
      

    resize = function() {
        width = $(document.getElementsByClassName(ACTIVE_CARD_CLASS)[0]).outerWidth()
        totalWidth = window.innerWidth * items.length;

        let index = currIndex;

        slider.style.transform = "translate3d(" + (((index * -width) + (width / 2) + window.innerWidth / 2) + (window.innerWidth *.015 )) + "px, 0, 0)";
  
        slider.style.width = totalWidth + "px";

        for (let i=1;i<items.length;i++){
            items[i].style.width = width
        }
    }

    showInactive = function(){
        if(membsLoaded == false){
            loadMembers(setInactive);
        }
        else{
            setInactive();
        }
    }
    
    setInactive = function(){
        let onScreenCards = document.getElementsByClassName(SMALL_CARD_CLASS)
        if(showInactives){
            let inactives = ''
            members.forEach(element => {
                if (element.isActive == false){
                    inactives += `${element.name} `
                }
      
            });
            if(sortByEvent){
            cards.forEach(cardSet => {
                cardSet.eventCards.forEach(element => {
                    if (inactives.includes(element.member)){
                       document.getElementById(`${element.eventcode}_${element.member}_${element.memberindex}`).classList.add(INACTIVE_CLASS)
                    }
                });
            });
            }
            else{
                cards.forEach(cardSet => {
                    cardSet.memberCards.forEach(element => {
                        console.log(element.member == 'inactive' ?  element : '' )
                        if (inactives.includes(element.member) || element.member == 'inactive'){
                           document.getElementById(`${element.eventcode}_${element.member}_${element.memberindex}`).classList.add(INACTIVE_CLASS)
                        }
                    });
                });
            }
            document.getElementById('inactiveIcon').innerHTML = 'T'
            document.getElementById('inactiveFilter').classList.add('activeFilter')
            showInactives = false;
        }
        else{
            document.getElementById('inactiveIcon').innerHTML = 'S'
            document.getElementById('inactiveFilter').classList.remove('activeFilter')
            Array.from(document.getElementsByClassName(INACTIVE_CLASS)).forEach(
                function(element, index, array) {
                    // do stuff
                    element.classList.remove(INACTIVE_CLASS)
                }
            );
            showInactives = true;
        }
    }

    setUpCards = function(){
        gridContent = ''
        let cardsDiv = document.getElementById(CARDSLIST_DIV_ID);
        cardsDiv.innerHTML = '';
        if (sortByEvent){

            let temp = []
            events.forEach(element =>{
                    let eventcards=[]
                    cards.forEach(item =>{
                        if(item.eventcode === element.eventCode){
                            eventcards.push(item)
                        }
                    })
                    let event= {
                        'eventName':element.eventName,
                        'eventCards':eventcards,
                    }

                    temp.push(event)
                
            });
            cards = temp;
            cardsDiv.innerHTML = gridContent;  
        }
        else{
            let temp = []
            let inactiveCards=[]
            members.forEach(element =>{
                if (element.isActive){
                    let membercards=[]
                    cards.forEach(item =>{
                        if(item.member === element.name){
                            membercards.push(item)
                        }
                    });


                    let member= {
                        'name':element.name,
                        'memberCards':membercards,
                    }

                    temp.push(member)
                } 
                else{
                    cards.forEach(item =>{
                        if(item.member === element.name){
                            inactiveCards.push(item)
                        }
                    });
                }
            });

            for(let i=1;i<=inactiveCards.length;i++){
                inactiveCards[i-1].eventindex = i;
                inactiveCards[i-1].member = 'inactive'
            }
            let inactiveMembers = {
                'name':'inactives',
                'memberCards':inactiveCards
            }
            temp.push(inactiveMembers)

            cards = temp;



        }

        cards.forEach(element => {
            if (element.eventName != undefined || element.memberCards != undefined){
                addCardList(element)
            }
        });

        cardsDiv.innerHTML = gridContent

    }

    setUpPopover = function(htmlElement){
       popContent = ''
       let popDiv = document.getElementById(SLIDER_ID)
       popDiv.innerHTML =''
       if(sortByEvent){
           let eventCards=[]
           cards.forEach(element => {
               if(element.eventCards[0].eventcode === htmlElement.getAttribute('data-event')){
                   addCardstoPopover(element.eventCards)
               }
           });
       }
       else{
            let memberCards=[]
            cards.forEach(element => {
                if(element.memberCards[0].member === htmlElement.getAttribute('data-member')){
                    addCardstoPopover(element.memberCards)
                }
            });
       }

       popDiv.innerHTML = popContent
    }


    showCards = function(element){
        setUpPopover(element);
        let modal = document.getElementById(MODAL_ID);
        let scrollTop = document.documentElement.scrollTop;
        $(modal).css({'display':'block','top':`${55}px`});
        
        resize()
        if(sortByEvent){
            switchCards(element.getAttribute(MEM_INDEX),0)
        }
        else{
            switchCards(element.getAttribute(EVENT_INDEX),0)
        }
        $(modal).animate({'opacity':1}, ANIMATION_DURATION_SHORT)

    }
  
    switchCards = function(index,duration=400) {
      
        if(index < 1) index = items.length;
        if(index > items.length) index = 1;
        currIndex = index;
      
        for(var i = 0; i < items.length; i++) {
            let card = items[i]
            let prevCard = items[i-1]
            let nextCard = items[i+1]
            let cardImg = card.getElementsByClassName(SLIDER_CARD_CLASS)[0];
            if(i == (index - 1)) {


                card.classList.add('activeCard');
                card.onclick =  function(){}

                if (prevCard !== undefined){
                    prevCard.onclick = function() { prev() };
                }
                if (nextCard !== undefined){
                    nextCard.onclick = function() { next() };
                }

                cardImg.style.transform = "perspective(1200px)"; 
            } else {

                card.classList.remove('activeCard');

                if (prevCard !== undefined){
                    prevCard.removeAttribute("onclick");
                }
                if (nextCard !== undefined){
                    nextCard.removeAttribute("onclick");
                }

                cardImg.style.transform = "perspective(1200px) rotateY(" + (i < (index - 1) ? 40 : -40) + "deg)";
            }
        }
        let transform = (((index * -width) + (width / 2) + window.innerWidth / 2) + (window.innerWidth *.015 ))
        // if(isInitial){
        //     slider.style.transform = "translate3d(" + (((index * -width) + (width / 2) + window.innerWidth / 2) + (window.innerWidth *.015 )) + "px, 0, 0)";
        // }

        if (slider.style.transform === undefined){
            slider.style.transform = 'translate3d(0,0,0)'
        }
        
        slider.animate([
            // keyframes
            { transform: slider.style.transform }, 
            { transform: `translate3d(${transform}px, 0, 0)` }
          ], { 
            // timing options
            duration: duration,
            iterations: 1
          });
          $(slider).css("transform","translate3d(" + transform + "px, 0, 0)");
    }
     
    toggleFilters = function(){
        let cardsDiv = document.getElementById(CARDSLIST_DIV_ID);
        let eventFilter = document.getElementById('eventFilter')
        let memberFilter = document.getElementById('memberFilter')
        $(cardsDiv).css({'transform':'translate(-100vw)'})
        if (sortByEvent){
            sortByEvent = false;
            eventFilter.classList.remove('activeFilter')
            eventFilter.setAttribute('onclick','toggleFilters()')
            memberFilter.classList.add('activeFilter')
            memberFilter.removeAttribute("onclick")

        }
        else{
            sortByEvent = true;
            eventFilter.classList.add('activeFilter')
            eventFilter.removeAttribute('onclick','toggleFilters()')
            memberFilter.classList.remove('activeFilter')
            memberFilter.setAttribute("onclick","toggleFilters()")
        }


        window.scrollTo(0,0)
        setTimeout(function(){
            loadCards();
            setTimeout(function(){
                if (showInactives){
                    showInactives = false
                }
                else{
                    showInactives = true
                }
                showInactive()
            },500)
            $(cardsDiv).css({'transform':'translate(0vw)'})
            cardsDiv.style= ''
        },500)

    }

    return {
        init,
        showCards,
        switchCards,
        closeModal,
        toggleFilters,
        showInactive,
    };
  }());
  