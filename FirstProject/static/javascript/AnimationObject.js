var Animation = {
    yielding: function* (elements){yield* elements;},
    drow:function(element,duration){
        var start = Date.now();
        var interval = setInterval(function () {
            var parantvisability = element.value.parentElement.classList.contains('hidden');
            if (!parantvisability){
                var timeround = (Date.now() - start) - ((Date.now() - start)%10);
                var timedelta = timeround / duration;
                Animation.TimingFunction(timedelta,element);
                if (timeround >= duration || parantvisability){clearInterval(interval)}
            } else {
                clearInterval(interval);
                Animation.StopAnimation()
            }
        },10);
    },
    Animate:function (nodeList,duration,delay) {
        this.links = nodeList; // глобальный параметр список элементов
        var items = this.yielding(nodeList);
        var timer = setInterval(function () {
            var item = items.next();
            if (item.done === true) {
                clearInterval(timer)
            } else {
                Animation.drow(item,duration)
            }
        },delay)
    },
    Coeff:2,
    TimingFunction:function (x,element) {
        let y,delim;
        delim = 4 * Math.PI; // количество отскоков напрямую зависит от коэффициента на который умножается PI
        if (this.Coeff === 2){
            y = Math.abs(((1/delim)/x)*Math.sin(delim*x))*this.Coeff;
        }
        if (y === 0){
            this.Coeff/=2;
        }
        if (x === 1){
            y = 0
        }
        y = y*115;
        element.value.style.transform = `translateX(${y +'px'})`;
    },
    StopAnimation:function () {
        for (let i of this.links) {
            i.removeAttribute('style')
        }
    }
};


        // function bounce(timeFraction) {
        //     for (let a = 0, b = 1; 1; a += b, b /= 2) {
        //         if ( timeFraction >= (7 - 4 * a) / 11 ) {
        //             return -Math.pow((11 - 6 * a - 11 * timeFraction) / 4, 2) + Math.pow(b, 2);
        //         }
        //     }
        // }
        // function makeEaseOut(timing) {
        //     return function (timeFraction) {
        //         return 1 - timing(1 - timeFraction);
        //     }
        // }
        // let bounceEaseOut = makeEaseOut(bounce);
