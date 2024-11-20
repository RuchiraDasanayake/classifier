import streamlit as st

# Set the title of the app
st.title('Machine Learning Model Creation Form')

# Create a form for model configuration
with st.form(key='ml_form'):
    # Model type selection
    model_type = st.selectbox('Select the model type', ['Linear Regression', 'Random Forest', 'SVM', 'KNN'])
    
    # Hyperparameters inputs for the model
    if model_type == 'Linear Regression':
        alpha = st.number_input('Alpha', min_value=0.01, max_value=10.0, step=0.01)
        fit_intercept = st.radio('Fit Intercept?', ['True', 'False'])
    elif model_type == 'Random Forest':
        n_estimators = st.number_input('Number of Estimators', min_value=10, max_value=1000, step=10)
        max_depth = st.number_input('Max Depth', min_value=1, max_value=20, step=1)
    elif model_type == 'SVM':
        C = st.number_input('C (Regularization Parameter)', min_value=0.01, max_value=10.0, step=0.01)
        kernel = st.selectbox('Kernel Type', ['linear', 'rbf', 'poly', 'sigmoid'])
    elif model_type == 'KNN':
        n_neighbors = st.number_input('Number of Neighbors', min_value=1, max_value=20, step=1)
        weights = st.selectbox('Weighting Function', ['uniform', 'distance'])
    
    # File upload
    file = st.file_uploader("Upload your dataset", type=["csv", "xlsx"])
    
    # Target column input
    target_column = st.text_input('Target column for prediction')
    
    # Submit button
    submit_button = st.form_submit_button(label='Build Model')
    
    # If the form is submitted, show the selected configuration
    if submit_button:
        st.write(f'Model Type: {model_type}')
        st.write(f'Target Column: {target_column}')
        if model_type == 'Linear Regression':
            st.write(f'Alpha: {alpha}')
            st.write(f'Fit Intercept: {fit_intercept}')
        elif model_type == 'Random Forest':
            st.write(f'Number of Estimators: {n_estimators}')
            st.write(f'Max Depth: {max_depth}')
        elif model_type == 'SVM':
            st.write(f'C: {C}')
            st.write(f'Kernel: {kernel}')
        elif model_type == 'KNN':
            st.write(f'Number of Neighbors: {n_neighbors}')
            st.write(f'Weighting Function: {weights}')
        if file:
            st.write(f'File uploaded: {file.name}')
