(function($){
    $(document).ready(function(){
        // Ranglar va o'lchamlar faqat yangi qo'shganlar uchun ko'rsatilsin
        $('.related-widget-wrapper').hide();  // Barcha ilgari qo'shilganlarni yashirish

        // "+" tugmasi bosilganda yangi qo'shish
        $('#id_color').on('change', function() {
            var selectedOption = $(this).val();
            if (selectedOption) {
                $(this).closest('div').find('.related-widget-wrapper').show(); // Yangi rangni ko'rsatish
            }
        });

        $('#id_size').on('change', function() {
            var selectedOption = $(this).val();
            if (selectedOption) {
                $(this).closest('div').find('.related-widget-wrapper').show(); // Yangi o'lchamni ko'rsatish
            }
        });
    });
})(django.jQuery);
