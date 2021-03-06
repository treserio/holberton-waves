let imageObj;
let quoteObj;
window.onload = () => {
  loadAllCarousels();
  loadquotes();
  // getQuotes();
}

function loadquotes() {
  if ($('.comments .carousel-inner').length) {

    $.ajax({
      url: 'https://randomuser.me/api/?results=10',
      dataType: 'json',
      beforeSend: () => {
        // Handle the beforeSend event
        $('.loader').show();
      },
      success: function(response01) {
        $.ajax({
          url: 'https://type.fit/api/quotes',
          dataType: 'json',
          success: function (response02) {

            imageObj = response01;
            quoteObj = response02;
            cmntList = [];
            for (let i = 0; i < 30; i++) {
              let quote = quoteObj[Math.floor(Math.random() * quoteObj.length - 1)];
              let user = imageObj.results[Math.floor(Math.random() * imageObj.results.length)]
              var name = user.name.first + ' ' + user.name.last;
              var picture = user.picture.large;

              cmntList.push(createCmnt(quote, name, picture));
            }
            oneStepCaro_nItems(cmntList, 1, $('.comments .carousel-inner'));
            $('.loader').hide();
            }
        })
        }
      });
    }
  }

function loadAllCarousels() {
  // load most popular videos from api
  if ($('.most-pop .pop-vids-4 .carousel-inner').length) {
    $.get('http://127.0.0.1:8000/api/?format=json&ordering=-likes', (data) => {
      // console.log('mostPopData', data);
      const cardList = [];
      for (let i = 0; i < 12; ++i) {
        cardList.push(createCard(data[i]));
      }
      // console.log(cardList);
      oneStepCaro_nItems(cardList, 4, $('.most-pop .pop-vids-4 .carousel-inner'));
      oneStepCaro_nItems(cardList, 2, $('.most-pop .pop-vids-2 .carousel-inner'));
      oneStepCaro_nItems(cardList, 1, $('.most-pop .pop-vids-1 .carousel-inner'));
    })
      .done(() => { $('.most-pop .loader').hide(); });
  }

  // if ($('.most-pop .pop-vids-4 .carousel-inner').length) {
  //   $.ajax({
  //     url: 'http://127.0.0.1:8000/api/?format=json&ordering=-likes',
  //     dataType: 'json',
  //     headers: {
  //       'Access-Control-Allow-Origin': '*'
  //     },
  //     success: (data) => {
  //       // console.log('mostPopData', data);
  //       const cardList = [];
  //       for (let i = 0; i < 12; ++i) {
  //         cardList.push(createCard(data[i]));
  //       }
  //       // console.log(cardList);
  //       oneStepCaro_nItems(cardList, 4, $('.most-pop .pop-vids-4 .carousel-inner'));
  //       oneStepCaro_nItems(cardList, 2, $('.most-pop .pop-vids-2 .carousel-inner'));
  //       oneStepCaro_nItems(cardList, 1, $('.most-pop .pop-vids-1 .carousel-inner'));
  //     }
  //   })
  //     .done(() => { $('.most-pop .loader').hide(); });
  // }

  // load latest videos from api
  if ($('.latest .pop-vids-4 .carousel-inner').length) {
    $.get('http://127.0.0.1:8000/api/?format=json&ordering=-published', (data) => {
      // console.log('latestData', data);
      const cardList = [];
      for (let i = 0; i < 12; ++i) {
        cardList.push(createCard(data[i]));
      }
      // console.log(cardList);
      oneStepCaro_nItems(cardList, 4, $('.latest .pop-vids-4 .carousel-inner'));
      oneStepCaro_nItems(cardList, 2, $('.latest .pop-vids-2 .carousel-inner'));
      oneStepCaro_nItems(cardList, 1, $('.latest .pop-vids-1 .carousel-inner'));
    })
      .done(() => { $('.latest .loader').hide(); });
  }

  // load courses section from api
  if ($('.results .row').length) {
    getCourses($('.results .row'));
    $('form.container').submit((e) => {
      e.preventDefault();
      getCourses($('.results .row'));
    });
  }
}

function createCmnt(quote, name, picture) {
  const cmnt = $('<div class="d-flex flex-column flex-md-row justify-content-around justify-content-md-center align-items-center">')[0];
  let cmntContent = `<div class="d-flex flex-column align-items-center">
                      <img class="rounded-circle" src="${picture}" alt="" width="160px" height="160px"></img>
                      <small class="mb-4 mt-2 mb-md-0">${name}</small>
                    </div>
                      <div class="comment-text ml-md-5 mr-md-0 flex-column text-center">
                        <div>?? ${quote.text}</div>
                        <h4 class="mt-2 mb-0">${quote.author}</h4>
                      </div>`;
  $(cmnt).append(cmntContent);
  return cmnt;
}

function createCard(info) {
  const card = $('<div class="card border-0"></div>')[0];
  let cardContent = `<div class="card-header">
      <a href="https://www.youtube.com/watch?v=${info.videoId}">
        <img src="${info.thumbnail}" width="255" height="154">
        <img class="play-btn" src="images/play.png" width="64" height="64">
      </a>
    </div>
    <div class="card-body">
      <h5 class="card-title mt-3"><b>${info.title}</b></h5>
      <small class="card-text">${info.description}</small>
      <div class="d-flex flex-row align-items-center mt-3">
        <img class="rounded-circle" src="${info.author_pic_url}" width="30" height="30">
        <small class="text-purple ml-2"><b>${info.author}</b></small>
      </div>
      <div class="d-flex flex-row align-items-center justify-content-between mt-2">
          <div>${info.likes} Likes</div>`;
  cardContent += `<small class="text-purple"><b>${info.duration}</b></small>
    </div>`;
  $(card).append(cardContent);
  return card;
}

function createTopicOption(info) {
  if (info == "All") {
    return $(`<option class="bg-white text-body" value="">${capFirstLtr(info)}</option>`)[0];
  }
  return $(`<option class="bg-white text-body" value="${info}">${capFirstLtr(info)}</option>`)[0];
}

function createOrderingOption(info) {
  if (info == "puplished") {
    return $(`<option class="bg-white text-body" value="-${info}">Most Recent</option>`)[0];
  }
  return $(`<option class="bg-white text-body" value="-${info}">${capFirstLtr(info)}</option>`)[0];
}

function oneStepCaro_nItems(cardList, nItems, target) {
  // console.log('cardList', cardList);
  // console.log('nItems', nItems);
  // console.log('target', target);
  for (let i = 0; i < cardList.length; ++i) {
    var carouselItem = $('<div class=carousel-item></div>')[0];
    // check for the correct type of object being added for parent settings
    if ($(cardList[0]).hasClass('card')) {
      var flexSetup = $('<div class="d-flex flex-row justify-content-around"></div>')[0];
    } else {
      var flexSetup = document.createDocumentFragment();
    }
    if (!i) {
      $(carouselItem).addClass('active');
    }
    for (let j = i; j < i + nItems; ++j) {
      flexSetup.append(cardList[j % cardList.length]);
    }
    carouselItem.append(flexSetup.cloneNode(true));
    target.append(carouselItem.cloneNode(true));
  }
}

function getCourses(target) {
  // clear out existing entries and show loader
  $('.results .loader').show();
  // console.log('target', target);
  $(target).empty();
  // grab all search parameters for api
  let keywords = $('#searchInput').val();
  let topic = $('#topicSelect').val();
  let sortBy = $('#exampleFormControlSelect1').val();
  // console.log('key:', keywords, 'top:', topic, 'sort:', sortBy);
  // set base api url
  let apiUrl = 'http://127.0.0.1:8000/api/?format=json'
  // fill with search parameters if present
  if (keywords) {
    apiUrl += `&search=${keywords}`;
  }
  if (topic) {
    apiUrl += `&topic=${topic}`;
  }
  if (sortBy) {
    apiUrl += `&ordering=${sortBy}`;
  }
  // console.log(apiUrl);
  $.get(apiUrl, (data) => {
      // console.log('coursesData', data);
      const cardList = [];
      const topicList = ['All'];
      const orderingList = ['likes', 'published', 'views', 'duration'];

      for (let item of data) {
        if (!(topicList.includes(item.topic))) {
          topicList.push(item.topic);
        }
        cardList.push(createCard(item));
      }
      // console.log('coursesList', cardList);
      let topics = $('.form-control#topicSelect')[0];
      let sorts = $('.form-control#exampleFormControlSelect1')[0];
      // check if the options are already there, if not fill them up!
      if (!topics.childElementCount) {
        // console.log('firing topics');
        for (let option of topicList) {
          $(topics).append(createTopicOption(option));
        }
      }
      if (!sorts.childElementCount) {

        for (let option of orderingList) {
          $(sorts).append(createOrderingOption(option));
        }
      }
      // add event listeners
      if (!$(topics).hasClass('listener')) {
        $(topics).addClass('listener');
        $(topics).on('change', () => $(topics).closest('form').submit());
      }
      if (!$(sorts).hasClass('listener')) {
        $(sorts).addClass('listener');
        $(sorts).on('change', () => $(sorts).closest('form').submit());
      }
      fillCourses(cardList, target);
    })
      .done(() => { $('.results .loader').hide(); });
}

function fillCourses(cardList, target) {
  // console.log('cardList', cardList);
  // console.log('target', target);
  for (card of cardList) {
    var wrapper = $('<div class="col-12 col-sm-6 col-md-4 col-lg-3 d-flex justify-content-center my-2">')[0];
    wrapper.append(card);
    target.append(wrapper.cloneNode(true));
  }
}

function capFirstLtr(string) {
  let words = string.split('_');
  return words.map((word) => {return word[0].toUpperCase() + word.substring(1)}).join(" ");
}

