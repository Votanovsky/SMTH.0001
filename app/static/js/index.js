console.log("load index.js")
// import gsap from "gsap";

// Анимация меню ===
const burger = document.querySelector('.burger')
const menu = document.querySelector('.menu')

console.log(gsap)

let tl = gsap.timeline();

tl.to(menu, {
    y: -300,
    display: 'none',
    duration: .5,
})

burger.addEventListener('click', () => {
    tl.reversed(!tl.reversed());
});


// Анимация скролл видео ===
const animation = document.querySelector('#animation')
const height = document.querySelector('#crutch')
const breakpoints = []
const breakpointsLength = 20

let count = 0

function playAnimation(event)
{
    if (count == breakpointsLength || event.deltaY / Math.abs(event.deltaY) < 0)
        return null
    animation.play()
    
    scrollTo({
        top: (count + 1) * height.clientHeight / breakpointsLength,
        behavior: 'smooth'
    })
    function checkTime()
    {
        if(animation.currentTime >= breakpoints[count])
        {
            animation.pause()
            count++
            return null
        }
        setTimeout(checkTime, 40)
    }
    checkTime()
}

animation.addEventListener('loadedmetadata', function() {
    this.style.position = "fixed"
    this.style.top = this.style.left = 0
    this.height = window.innerHeight
    this.width = window.innerWidth
    // Изначально ставим видео на паузу
    this.pause()
    // Создаём n брейкпойнтов для анимации
    for(let i = 0; i < breakpointsLength; i++)
        breakpoints.push((i + 1) * animation.duration / breakpointsLength)
    // Даём странице полвысоты экрана пользователя на каждый брейкпоинт
    height.style.height = 20 * breakpointsLength + "vh"
    // Регулируем событие изменения масштаба
    window.addEventListener('resize', function() {
        animation.height = window.innerHeight
        animation.width = window.innerWidth
    })
    window.addEventListener('wheel', playAnimation)
    window.addEventListener('touchmove', playAnimation)
})

window.onbeforeunload = function() {
    scrollTo({top: 0, behavior: 'instant'})
}