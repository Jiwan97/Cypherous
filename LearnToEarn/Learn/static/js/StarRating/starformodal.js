
$( document ).ready(function() {

    const one = document.getElementById('0')
    const two = document.getElementById('1')
    const three = document.getElementById('2')
    const four = document.getElementById('3')
    const five = document.getElementById('4')


    const form = document.querySelector('.rate-form')
    const rateValue = document.getElementById('rate_value1')

    const handleStarSelect = (size) => {
        const children = form.children
        console.log(children[0])
        for (let i=0; i < children.length; i++) {
            if(i <= size) {
                children[i].classList.add('checked')
            } else {
                children[i].classList.remove('checked')
            }
        }
    }

    const handleSelect = (selection) => {
        switch(selection){
            case '0': {
                one.classList.add('checked','bigStar')
                two.classList.remove('checked')
                three.classList.remove('checked')
                four.classList.remove('checked')
                five.classList.remove('checked')

                return
            }
            case '1': {
                one.classList.add('checked')
                two.classList.add('checked','bigStar')
                three.classList.remove('checked')
                four.classList.remove('checked')
                five.classList.remove('checked')
                return
            }
            case '2': {
                one.classList.add('checked')
                two.classList.add('checked')
                three.classList.add('checked','bigStar')
                four.classList.remove('checked')
                five.classList.remove('checked')
                return
            }
            case '3': {
                one.classList.add('checked')
                two.classList.add('checked')
                three.classList.add('checked')
                four.classList.add('checked','bigStar')
                five.classList.remove('checked')
                return
            }
            case '4': {
                one.classList.add('checked')
                two.classList.add('checked')
                three.classList.add('checked')
                four.classList.add('checked')
                five.classList.add('checked','bigStar')
                return
            }
            default: {
                handleStarSelect(0)
            }
        }

    }

    const getNumericValue = (stringValue) =>{
        let numericValue;
        if (stringValue === '0') {
            numericValue = 1
        }
        else if (stringValue === '1') {
            numericValue = 2
        }
        else if (stringValue === '2') {
            numericValue = 3
        }
        else if (stringValue === '3') {
            numericValue = 4
        }
        else if (stringValue === '4') {
            numericValue = 5
        }
        else {
            numericValue = 0
        }
        return numericValue
    }

    if (one) {
        const arr = [one, two, three, four, five]

        arr.forEach(item=> item.addEventListener('mouseover', (event)=>{
            handleSelect(event.target.id)
        }));
        arr.forEach(item=> item.addEventListener('click', (event)=>{
            const val = event.target.id
            const val_num = getNumericValue(val)
            console.log(val)
            console.log(val_num)
            rateValue.value= val_num
        }));
        arr.forEach(item=> item.addEventListener('mouseout', (event)=>{
            one.classList.remove('bigStar','checked')
            two.classList.remove('bigStar','checked')
            three.classList.remove('bigStar','checked')
            four.classList.remove('bigStar','checked')
            five.classList.remove('bigStar','checked')
            if (rateValue.value === '1') {
                one.classList.add('checked')
            }
            else if (rateValue.value === '2') {
                one.classList.add('checked')
                two.classList.add('checked')
            }
            else if (rateValue.value === '3') {
                one.classList.add('checked')
                two.classList.add('checked')
                three.classList.add('checked')
            }
            else if (rateValue.value === '4') {
                one.classList.add('checked')
                two.classList.add('checked')
                three.classList.add('checked')
                four.classList.add('checked')
            }
            else if (rateValue.value === '5') {
                one.classList.add('checked')
                two.classList.add('checked')
                three.classList.add('checked')
                four.classList.add('checked')
                five.classList.add('checked')
            }
        }));

    };
});