function maskPhone(event) {
    let input = event.target;
    let value = input.value.replace(/\D/g, ''); // Remove tudo que não é dígito
    let finalValue = '';
    
    // Verifica se é celular (tem 9 como primeiro dígito após DDD)
    const isCellPhone = value.length > 2 && value.charAt(2) === '9';
    
    if (value.length <= 10 && !isCellPhone) {
        // Formato: (XX) XXXX-XXXX
        if (value.length > 2) {
            finalValue += '(' + value.substring(0, 2) + ') ';
        } else {
            finalValue += '(' + value;
        }
        
        if (value.length > 2) {
            finalValue += value.substring(2, 6);
        } else if (value.length > 6) {
            finalValue += value.substring(2, 6) + '-';
        }
        
        if (value.length > 6) {
            finalValue += '-' + value.substring(6, 10);
        }
        
    } else {
        // Formato: (XX) XXXXX-XXXX
        if (value.length > 2) {
            finalValue += '(' + value.substring(0, 2) + ') ';
        } else {
            finalValue += '(' + value;
        }
        
        if (value.length > 2) {
            finalValue += value.substring(2, 7);
        }
        
        if (value.length > 7) {
            finalValue += '-' + value.substring(7, 11);
        }
    }
    
    input.value = finalValue;
}

// Função para aplicar a máscara a um elemento input
function applyPhoneMask(inputElement) {
    inputElement.addEventListener('input', maskPhone);
    
    // Limita o tamanho máximo
    inputElement.setAttribute('maxlength', '15');
    
    // Aplica a máscara a qualquer valor inicial
    let event = new Event('input');
    inputElement.dispatchEvent(event);
}


function maskDate(event) {
    let input = event.target;
    let value = input.value.replace(/\D/g, ''); // Remove tudo que não é dígito
    let finalValue = '';
    
    if (value.length > 0) {
        // Primeiro digito não pode ser maior que 3
        if (value.charAt(0) > 3) {
            return;
        }
        
        // Dia não pode ser maior que 31
        if (value.length >= 2) {
            const day = parseInt(value.substring(0, 2));
            if (day > 31 || day === 0) {
                return;
            }
        }
        
        // Mês não pode ser maior que 12
        if (value.length >= 4) {
            const month = parseInt(value.substring(2, 4));
            if (month > 12 || month === 0) {
                return;
            }
        }
        
        // Formata DD/MM/YYYY
        if (value.length > 2) {
            finalValue += value.substring(0, 2) + '/';
        } else {
            finalValue += value;
        }
        
        if (value.length > 4) {
            finalValue += value.substring(2, 4) + '/';
        } else if (value.length > 2) {
            finalValue += value.substring(2, 4);
        }
        
        if (value.length > 4) {
            finalValue += value.substring(4, 8);
        }
    }
    
    input.value = finalValue;
}

// Função para validar uma data
function isValidDate(dateString) {
    const parts = dateString.split('/');
    if (parts.length !== 3) return false;
    
    const day = parseInt(parts[0]);
    const month = parseInt(parts[1]) - 1; // Mês começa do 0 no JavaScript
    const year = parseInt(parts[2]);
    
    const date = new Date(year, month, day);
    
    return date.getDate() === day &&
           date.getMonth() === month &&
           date.getFullYear() === year &&
           year >= 1900 && // Valida ano mínimo
           year <= new Date().getFullYear(); // Não permite anos futuros
}

// Função para aplicar a máscara a um elemento input
function applyDateMask(inputElement) {
    inputElement.addEventListener('input', maskDate);
    
    // Limita o tamanho máximo
    inputElement.setAttribute('maxlength', '10');
    
    // Adiciona validação no blur
    inputElement.addEventListener('blur', function() {
        if (this.value && !isValidDate(this.value)) {
            this.classList.add('invalid');
            this.setCustomValidity('Data inválida');
        } else {
            this.classList.remove('invalid');
            this.setCustomValidity('');
        }
    });
    
    // Aplica a máscara a qualquer valor inicial
    let event = new Event('input');
    inputElement.dispatchEvent(event);
}

// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    // Add click event listener to all elements with the delete class
    document.querySelectorAll('.delete-item').forEach(function(link) {
        link.addEventListener('click', function(event) {
            event.preventDefault();
            
            // Get the href from the link
            const deleteUrl = this.getAttribute('href');            
            const confirmed = confirm('Tem certeza que deseja excluir este item?');
            
            // If user confirms, proceed with deletion
            if (confirmed) {
                window.location.href = deleteUrl;
            }
        });
    });

    // Aplica a máscara a todos os inputs com a classe 'phone-mask'
    document.querySelectorAll('.phone-mask').forEach(function(input) {
        applyPhoneMask(input);
    });

    // Aplica a máscara a todos os inputs com a classe 'date-mask'
    document.querySelectorAll('.date-mask').forEach(function(input) {
        applyDateMask(input);
    });
});
