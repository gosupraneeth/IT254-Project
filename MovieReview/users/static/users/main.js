

function toogle_active(obj) {
    if (!obj.classList.contains('b_active')) {
        obj.classList.add('b_active');
    }
    else {
        obj.classList.remove('b_active');
    }
    b_active_btns = document.querySelectorAll('.b_active');
    if (btn_count != b_active_btns.length) {
        btn_count = b_active_btns.length;
        counter = 1;
        btn_flag = 0;
    }
    get_data_g_l(b_active_btns);
};




function myFunction() {
    var dots;
    var moreText;
    var btnText;
    var parent;
    document.querySelectorAll('.myBtn').forEach((button) => {
        button.onclick = function () {
            parent = this.parentNode;
            dots = parent.getElementsByClassName('dots')[0];
            moreText = parent.getElementsByClassName("more")[0];
            btnText = parent.getElementsByClassName("myBtn")[0];

            if (dots.style.display === "none") {
                dots.style.display = "inline";
                btnText.innerHTML = "Read more";
                moreText.style.display = "none";
            } else {
                dots.style.display = "none";
                btnText.innerHTML = "Read less";
                moreText.style.display = "inline";
            }
        }
    });
}




if (!localStorage.getItem('darktheme')) {

    // If not, set the counter to 0 in local storage
    localStorage.setItem('darktheme', false);
}
document.addEventListener('DOMContentLoaded', () => {
    if (localStorage.getItem('darktheme') == 'true') {
        document.getElementById('flexSwitchCheckChecked').checked = true;
        localStorage.setItem('darktheme', false);
    } else {
        document.getElementById('flexSwitchCheckChecked').checked = false;
        localStorage.setItem('darktheme', true);
    }
    //var element = document.body;
    //element.classList.add("dark-mode");
    changeTheme();
});

function changeTheme() {
    let theme = localStorage.getItem('darktheme');
    var setbool;
    if (theme == "true") {
        setbool = false;
        var element = document.body;
        element.classList.add("dark-mode");
    }
    else {
        setbool = true;
        var element = document.body;
        element.classList.remove("dark-mode");
    }
    localStorage.setItem('darktheme', setbool);
};
function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
};

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
};

function sidenav(x) {
    if (x.matches) {
        closeNav();
    }

};

window.addEventListener('resize', () => {
    var x = window.matchMedia("(min-width: 1000px)");
    sidenav(x);
    x.addListener(sidenav);
});




document.addEventListener('DOMContentLoaded', () => {
    var current = null;
    document.querySelector('.username').addEventListener('focus', function () {
        if (current) current.pause();
        current = anime({
            targets: 'path',
            strokeDashoffset: {
                value: 0,
                duration: 700,
                easing: 'easeOutQuart'
            },
            strokeDasharray: {
                value: '443 1386',
                duration: 700,
                easing: 'easeOutQuart'
            }
        });
    });
    document.querySelector('.password').addEventListener('focus', function (e) {
        if (current) current.pause();
        current = anime({
            targets: 'path',
            strokeDashoffset: {
                value: -555,
                duration: 700,
                easing: 'easeOutQuart'
            },
            strokeDasharray: {
                value: '440 1386',
                duration: 700,
                easing: 'easeOutQuart'
            }
        });
    });
    document.querySelector('.login_submit').addEventListener('focus', function (e) {
        if (current) current.pause();
        current = anime({
            targets: 'path',
            strokeDashoffset: {
                value: -1300,
                duration: 500,
                easing: 'easeOutQuart'
            },
            strokeDasharray: {
                value: '420 1786',
                duration: 700,
                easing: 'easeOutQuart'
            }
        });
    });
});

function capitalizeFirstLetter(string) {
    return string.charAt(0).toUpperCase() + string.slice(1);
}


function load_val_data(val) {
    MOOD = ["happy", "sad", "upset", "worry", "excited", "silly", "frustrated", "scared", "angry"];
    GENRE = ["Action", "Adventure", "Darkmovies", "Drama", "Fantasy", "Musical", "Romance", "Sci-Fi", "Thriller", "Comedy", "History"];
    LANGUAGE = ["Hindi", "Marathi", "English", "French", "German", "Spanish", "Russian", "Italian", "Japanese", "Chinese"];
    let ano_val = capitalizeFirstLetter(val);
    if (LANGUAGE.includes(val)) {
        localStorage.setItem('lang', val);
        console.log(val);
    }
    if (LANGUAGE.includes(ano_val)) {
        localStorage.setItem('lang', ano_val);
        console.log(val);
    }
    if (MOOD.includes(val)) {
        var mood_div = document.createElement('div');
        mood_div.classList.add('mood-div');
        if (document.querySelector('.mood-div') != null) {
            document.querySelector('.mood-div').remove();
        }
        var lang = localStorage.getItem('lang');
        mood_div.innerHTML = `<div class="load-3">
                                <div class="line"></div>
                                <div class="line"></div>
                                <div class="line"></div>
                                </div>`
        document.querySelector('.chats').append(mood_div);
        setTimeout(() => {
            fetch(`/getchat_mood?mood=${val}&lang=${lang}`)
                .then(response => response.json())
                .then(data => {
                    data.cards.forEach(add_chat_post);
                })
        }, 10);
    }
    if (GENRE.includes(val)) {
        var genre_div = document.createElement('div');
        genre_div.classList.add('genre-div');
        if (document.querySelector('.genre-div') != null) {
            document.querySelector('.genre-div').remove();
        }
        var lang = localStorage.getItem('lang');
        genre_div.innerHTML = `<div class="load-3">
                                <div class="line"></div>
                                <div class="line"></div>
                                <div class="line"></div>
                                </div>`
        document.querySelector('.chats').append(genre_div);
        setTimeout(() => {
            fetch(`/getchat_genre?genre=${val}&count=${6}&lang=${lang}`)
                .then(response => response.json())
                .then(data => {
                    data.cards.forEach(add_chat_post_genre);
                })
        }, 10);
    }
    console.log(val);
};
function add_chat_post(contents) {
    if (document.querySelector('.load-3') != null) {
        document.querySelector('.load-3').remove();
    }
    var chat_card = document.createElement('div');
    chat_card.classList.add('chat-card');
    chat_card.innerHTML = `<a href="#" onclick="get_single_card('${contents.mid}')" style="text-decoration:None;color:White">${contents.title} <br> Rating:${contents.rating}<a>`;
    document.querySelector('.mood-div').append(chat_card);
};
function add_chat_post_genre(contents) {
    if (document.querySelector('.load-3') != null) {
        document.querySelector('.load-3').remove();
    }
    var chat_card = document.createElement('div');
    chat_card.classList.add('chat-card');
    chat_card.innerHTML = `<a href="#" onclick="get_single_card('${contents.mid}')" style="text-decoration:None;color:White">${contents.title} <br> Rating:${contents.rating}<a>`;
    document.querySelector('.genre-div').append(chat_card);
};




function search_post() {
    var m_name = document.querySelector("#search").value;
    fetch(`/searchbar?m_name=${m_name}`)
        .then(response => response.json())
        .then(data => {
            data.cards.forEach(add_single_post);
        })
};



function get_single_card(mid) {
    //document.querySelectorAll('.cards-box')
    fetch(`/get_single_card?mid=${mid}`)
        .then(response => response.json())
        .then(data => {
            data.cards.forEach(add_single_post);
        })
};



var count = 1;
var temp = 0;
function set_image() {
    images = document.querySelectorAll('.chat-buttons > .chat-button > div > span');
    for (i = 0; i < images.length; i++) {
        if (images[i].childElementCount == 0) {
            images[i].innerHTML = images[i].textContent || images[i].innerHTML
        }
    }
    document.querySelectorAll('.chat-button').forEach((btn) => {
        if ("chat-button-disabled" == btn.classList[1]) {
            btn.removeAttribute("onclick");
        }
        else {
            bl = btn.querySelector('div > span');
            if (bl.childElementCount == 0) {
                btn.setAttribute("onclick", "load_val_data(this.querySelector('div > span').innerHTML)");
            }
            else {
                btn.setAttribute("onclick", "load_val_data(this.querySelector('div > span >img').alt)");
            }
        }

    });
};

function count_ele() {
    block_chats = document.querySelector('.chats');
    if (block_chats.childElementCount != count) {
        count = block_chats.childElementCount;
        set_image();
    }
};
document.addEventListener('DOMContentLoaded', () => {
    var timer1 = setInterval(set_image, 10);
});




document.addEventListener('DOMContentLoaded', load);
const quantity = 5;
let counter = 1;
let counter_genre = 1;
let counter_lang = 1;
function check() {
    listElm = document.querySelector('.cards-box');
    if (listElm.scrollTop + listElm.clientHeight >= listElm.scrollHeight - 1) {
        document.querySelector('.modal').style.display = "none";
        document.querySelector('.modal').style.display = "block";
        setTimeout(() => {
            b_active_btns = document.querySelectorAll('.b_active');
            if (b_active_btns.length == 0) {
                load();
            }
            else {
                btn_flag = 1;
                get_data_g_l(b_active_btns);
            }
        }, 1200);
    }
};
window.addEventListener('scroll', check);

// Load next set of posts
function load() {
    // Set start and end post numbers, and update counter
    const start = counter;
    const end = start + quantity - 1;
    counter = end + 1;
    console.log(`start='${start}' end='${end}' %}`);
    // Get new posts and add posts
    fetch(`/getdata?start=${start}&end=${end}`)
        .then(response => response.json())
        .then(data => {
            data.cards.forEach(add_post);
        })
    document.querySelector('.modal').style.display = "none";
};

// Add a new post with given contents to DOM




document.addEventListener('DOMContentLoaded', () => {
    document.querySelector(".input").setAttribute('onclick', 'input_fetch_data()');
    document.querySelector(".input input[type='submit']").setAttribute('onclick', 'input_fetch_data()');
});

function input_fetch_data() {
    var val = document.querySelector(".input > input[type='text']").value;
    load_val_data(val.toLowerCase());
};



let btn_count = 0;
let btn_flag = 0;
function get_data_g_l(btns) {
    const quantity = 5;
    const start = counter;
    const end = start + quantity - 1;
    counter = end + 1;
    GENRE = ["Action", "Adventure", "DarkMovies", "Drama", "Fantasy", "Musical", "Romance", "Scifi", "Thriller", "Comedy", "History"];
    LANGUAGE = ["Hindi", "Marathi", "English", "French", "German", "Spanish", "Russian", "Italian", "Japanese", "Chinese"];
    var lang = new Array();
    var genre = new Array();
    for (i = 0; i < btns.length; i++) {
        if (LANGUAGE.includes(btns[i].innerText)) {
            lang.push(btns[i].innerText);
        }
        if (GENRE.includes(btns[i].innerHTML)) {
            genre.push(btns[i].innerHTML);
        }
    }
    if (btn_flag == 0) {
        document.querySelector('.cards-box').innerHTML = '';
    }
    console.log(start, end);
    fetch(`/get_data_g_l?start=${start}&end=${end}&lang=${lang}&genre=${genre}`)
        .then(response => response.json())
        .then(data => {
            data.cards.forEach(add_post);
        })
    document.querySelector('.modal').style.display = "none";
};

function remove_all() {
    document.querySelectorAll('.b_active').forEach(btn => {
        btn.classList.remove('b_active');
    });
    load();
}