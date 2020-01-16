//Let's explore some events samples!

var headOne = document.querySelector('#one');
var headTwo = document.querySelector('#two');
var headThree = document.querySelector('#three');

// Hover (mouseover and mouseout)
headOne.addEventListener('mouseover',function(){
  headOne.textContent = "Mouse currently Over";
  headOne.style.color = 'red';
});

headOne.addEventListener('mouseout',function(){
  headOne.textContent = "Mouse Not On me.";
  headOne.style.color = 'blue';
});


// On Click
headTwo.addEventListener("click",function(){
  headTwo.textContent = "Clicked On";
  headTwo.style.color = 'blue';
});

headTwo.addEventListener("mouseout",function(){
  headTwo.textContent = "Click Me!";
  headTwo.style.color = 'black';
});




// Double Click
headThree.addEventListener("dblclick",function(){
  headThree.textContent = "Double Clicked!";
  headThree.style.color = 'red';
});

headThree.addEventListener("mouseout",function(){
  headThree.textContent = "Double Click Me!";
  headThree.style.color = 'black';
});
