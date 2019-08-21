https://codepen.io/rzim2082/pen/jrWYJW

var question = prompt(chara + ", has awoken on the beach of the hidden isalnd you have been looking for! You have almost no resources to survive the night what do you do next!?")
var images = document.getElementById("images"); 
var text = document.getElementById("text");
var buttonBox = document.getElementById('buttonBox');
var input = document.getElementById('input');
var chara;



input.onkeypress = function(event) {
  console.log(input.value);
  if (event.key == "Enter" || event.keyCode == 13) {
    yerdog =  input.value;
    input.parentNode.removeChild(input)
    advanceTo(scenario.two)
  }
};


var changeText = function(words) {
  text.innerHTML = words.replace("Character", chara);
};

var changeImage = function(img) {
  images.style.backgroundImage = "url(" + img + ")";
};


var changeButtons = function(buttonList) {
  buttonBox.innerHTML = "";
  for (var i = 0; i < buttonList.length; i++) {
    buttonBox.innerHTML += "<button onClick="+buttonList[i][1]+">" + buttonList[i][0] + "</button>";
  };
};

var advanceTo = function(s) {
  changeImage(s.image)
  changeText(s.text)
  changeButtons(s.buttons)
};


var scenario = {
  one: {
    image: "",
    text: "\n",
  },
  two: {
    image: "",
    text: "",
    buttons: [["", "advanceTo(scenario.three)"],["", "advanceTo(scenario.four)"]]
  },
  three: {
    image: "",
    text: "",
    buttons: [["continue", "advanceTo(scenario.four)"]]
  },
    four: {
    image: "",
    text: "",
    buttons: [["", "advanceTo(scenario.five)"],["", "advanceTo(scenario.five)"]]
  },
    five: {
    image: "",
    text: "",

  },

};



advanceTo(scenario.one);
