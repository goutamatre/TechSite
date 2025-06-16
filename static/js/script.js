document.addEventListener('DOMContentLoaded', () => {
  const track = document.querySelector('.carousel-track');
  const cards = document.querySelectorAll('.alumni-card');
  const dotsContainer = document.querySelector('.carousel-dots');
  const cardWidth = cards[0].offsetWidth + 20; // card + margin
  const totalCards = cards.length;
  let currentIndex = 0;

  // Create dot buttons based on each card
  for (let i = 0; i < totalCards; i++) {
    const dot = document.createElement('button');
    if (i === 0) dot.classList.add('active');
    dot.addEventListener('click', () => {
      currentIndex = i;
      updateCarousel();
    });
    dotsContainer.appendChild(dot);
  }

  function updateCarousel() {
    const offset = currentIndex * cardWidth;
    track.style.transform = `translateX(-${offset}px)`;
    dotsContainer.querySelectorAll('button').forEach((dot, i) => {
      dot.classList.toggle('active', i === currentIndex);
    });
  }

  setInterval(() => {
    currentIndex = (currentIndex + 1) % totalCards;
    updateCarousel();
  }, 3000); // auto-scroll every 3 seconds
});

// Lightbox functionality
document.addEventListener('DOMContentLoaded', () => {
  const lightbox = document.getElementById('lightbox');
  const lightboxImg = document.getElementById('lightbox-img');
  const closeBtn = document.querySelector('.close');

  document.querySelectorAll('.gallery-item img').forEach(img => {
    img.addEventListener('click', () => {
      lightbox.style.display = 'block';
      lightboxImg.src = img.src;
    });
  });

  closeBtn.addEventListener('click', () => {
    lightbox.style.display = 'none';
  });

  // Close when clicking outside the image
  lightbox.addEventListener('click', e => {
    if (e.target === lightbox) {
      lightbox.style.display = 'none';
    }
  });
});

// cse table section
function showTab(tabId, el) {
  const tabs = document.querySelectorAll('.tab-content');
  const buttons = document.querySelectorAll('.tab-btn');

  // Hide all tab contents
  tabs.forEach(tab => tab.classList.remove('active'));

  // Remove active class from all buttons
  buttons.forEach(button => button.classList.remove('active'));

  // Show the selected tab
  const targetTab = document.getElementById(tabId);
  if (targetTab) {
    targetTab.classList.add('active');
  }

  // Add active class to the clicked button
  if (el) {
    el.classList.add('active');
  }
}





// Inject navbar and footer into page
document.addEventListener('DOMContentLoaded', () => {
  fetch('/templates/includes/navbar.html')
    .then(res => res.text())
    .then(data => {
      document.getElementById('navbar-placeholder').innerHTML = data;

      // Add active class dynamically
      const currentPage = window.location.pathname.split('/').pop(); // e.g. about.html
      const navLinks = document.querySelectorAll('.nav-links a');
      navLinks.forEach(link => {
        if (link.getAttribute('href').includes(currentPage)) {
          link.classList.add('active');
        }
      });
    });

  fetch('/templates/includes/footer.html')
    .then(res => res.text())
    .then(data => {
      document.getElementById('footer-placeholder').innerHTML = data;
    });
});
