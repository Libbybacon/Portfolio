// Open Modal
function openModal() {
    document.getElementById("myModal").style.display = "block";
}

// Close Modal
function closeModal() {
    document.getElementById("myModal").style.display = "none";
}

var slideIndex = 1; // set initial slide index value to 1
showSlides(slideIndex); //call showSlides function

// Next/Previous Controls
function plusSlides(n) {
    showSlides(slideIndex += n);
}

// Thumbnail Image Controls
function currentSlide(n) {
    showSlides(slideIndex = n);
}

// Show Slides Function
function showSlides(n) {
    var i;
    // Set variable equal to array of mySlides
    var slides = document.getElementsByClassName("mySlides");
    var dots = document.getElementsByClassName("demo");
    var captionText = document.getElementById("caption");
    // Return to slide one when you press next on last slide
    if (n > slides.length) { slideIndex = 1 }
    if (n < 1) { slideIndex = slides.length }
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    // Give active properties to dot that corresponds to current active slide
    for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "");//Change thumbnail attribute from active to inacative
    }
    slides[slideIndex-1].style.display = "block"; // Display current slide as block
    dots[slideIndex-1].className += " active";
    captionText.innerHTML = dots[slideIndex-1].alt; // Assign alt value to captionText
} 