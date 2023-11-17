import streamlit as st
from datetime import datetime

def main():
    st.title('NDVI')

    day = ['01', '11', '21']

    # Sidebar for user input
    selected_year = st.sidebar.selectbox('Selecione o ano', range(2011, (datetime.now().year) + 1), index=0)
    selected_month = st.sidebar.selectbox('Selecione o mês', range(1, 13), index=0)
    selected_day = st.sidebar.selectbox('Selecione o dia', day, index=0)

    # Create a datetime object for the selected date
    selected_date = datetime(selected_year, selected_month, int(selected_day))

    # Check if the selected date is in the future
    if selected_date > datetime.now():
        st.error("Esta imagem ainda não está disponível")
    else:
        root_folder = 'https://barramento2.apac.pe.gov.br/satelite/ndvi/'
        url = f'{root_folder}/{selected_year}/{selected_month:02d}/{selected_day}/METOP_AVHRR_{selected_year}{selected_month:02d}{selected_day}_S10_AMs_NDV.png'

        # Display the image
        st.image(f'{url}', caption='Image', use_column_width=True)

if __name__ == '__main__':
    main()

