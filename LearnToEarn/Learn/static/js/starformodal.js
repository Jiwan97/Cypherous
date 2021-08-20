
$( document ).ready(function() {

    const one = document.getElementById('fir')
    const two = document.getElementById('sec')
    const three = document.getElementById('thi')
    const four = document.getElementById('fou')
    const five = document.getElementById('fif')


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
            case 'fir': {
                one.classList.add('checked')
                two.classList.remove('checked')
                three.classList.remove('checked')
                four.classList.remove('checked')
                five.classList.remove('checked')

                return
            }
            case 'sec': {
                one.classList.add('checked')
                two.classList.add('checked')
                three.classList.remove('checked')
                four.classList.remove('checked')
                five.classList.remove('checked')
                return
            }
            case 'thi': {
                one.classList.add('checked')
                two.classList.add('checked')
                three.classList.add('checked')
                four.classList.remove('checked')
                five.classList.remove('checked')
                return
            }
            case 'fou': {
                one.classList.add('checked')
                two.classList.add('checked')
                three.classList.add('checked')
                four.classList.add('checked')
                five.classList.remove('checked')
                return
            }
            case 'fif': {
                one.classList.add('checked')
                two.classList.add('checked')
                three.classList.add('checked')
                four.classList.add('checked')
                five.classList.add('checked')
                return
            }
            default: {
                handleStarSelect(0)
            }
        }

    }

    const getNumericValue = (stringValue) =>{
        let numericValue;
        if (stringValue === 'fir') {
            numericValue = 1
        }
        else if (stringValue === 'sec') {
            numericValue = 2
        }
        else if (stringValue === 'thi') {
            numericValue = 3
        }
        else if (stringValue === 'fou') {
            numericValue = 4
        }
        else if (stringValue === 'fif') {
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
            const val = event.target.id
            const val_num = getNumericValue(val)
            console.log(val)
            console.log(val_num)
            rateValue.innerHTML= val_num
        }))

    }
});