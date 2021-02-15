
    let scrollLink = document.querySelectorAll('.scroll-link')
    let navbar = document.querySelector('.navbar')
    let linksContainer = document.querySelector('.links-container')
    scrollLink.forEach(function(link){
    link.addEventListener('click',function(e){
        e.preventDefault();
        let id = link.getAttribute('href').slice(2);
        // console.log("Id : " + id)
        let element = document.getElementById(id);
        // console.log("Element : "+ element)
        // console.log("Offset : " + element.offsetTop)
        let navbarHeight = navbar.getBoundingClientRect().height;
        let containerHeight = linksContainer.getBoundingClientRect().height;
        let position = element.offsetTop - navbarHeight;
        if(navbarHeight>112)
        {
            position=position+containerHeight
        }
        window.scrollTo({
            left:0,
            top:position
        })
        linksContainer.style.height=`0px`;
    })
})

