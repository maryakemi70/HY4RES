import os
import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

# --- Terminal: Run App ---
#cd C:\Users\Win\PycharmProjects\pythonProject\Streamlit
#streamlit run streamlit_app.py

# --- Page Configuration ---
st.set_page_config(
    layout="wide",
    page_title="Results WP2.1. HY4RES Project",
    page_icon="🌱")

# --- Dictionaries with information ---
pilot_text = {
    "Irrigation System, Spain": " The pilot site related to the agricultural sector will be constructed in the Valle Inferior irrigation community, located in the Guadalquivir River Basin in Andalusia, Spain. This irrigation system has an area of 18,945 hectares, extending from the town of Lora del Río to the city of Seville. The system counts about 2300 irrigators and 3000 plots.",
    "Fish Farm, Ireland": "Located in the North-West of Ireland, in County Donegal, the HY4RES aquaculture pilot site will implement a hybrid renewable energy system combining wind and hydro power. This hybrid system combined with an intelligent management software will enable to maximise the production and use of renewable energy in a fish processing plant.",
    "Port of Avilés, Spain": "Located in the port of Avilés in Northern Spain, the HY4RES port pilot site will implement a hybrid renewable energy system for electricity production, combining solar, wind and hydropower at micro-scale, and designed using the tools and software developed as part of the project.",
    "Energy Community, Portugal": "The pilot site at Castanheira de Pera and Marruge in Portugal concerns a community energy. The aim is to install a hybrid renewable energy system and implement a software to manage the community’s energy needs. The system uses water from the small stream, solar energy captured on the surrounding slopes, and wind energy. Thanks to HY4RES project, the objective is to enable the supply of the needed energy from renewable sources to run the village of Marruge."
}

objectives_pilot_text = {
    "Irrigation System, Spain": (
        "- Maximizing the use of renewable energy sources, thereby minimizing the use of conventional energy sources and decreasing the energy costs for irrigation;\n"
        "- Minimizing greenhouse gas emissions by replacing conventional energy sources by renewable energy sources;\n"
        "- Using the obtained results of the agricultural sector in other sectors of the HY4RES project (aquaculture, port and energy community sectors), and thereby contributing to the overall project objective: increasing the penetration of renewable energy sources in the Atlantic Area"),

    "Fish Farm, Ireland": (
        "- Demonstrate the potential for decarbonisation of the aquaculture sector using multiple energy sources (wind, hydro, biomass)\n"
        "- Measure and balance supply and demand from these variable output sources electricity, measure energy storage capacity and opportunities\n"
        "- Demonstrate the potential for optimising the management of available renewable energy sources, saving costs, and reducing emissions."),

    "Port of Avilés, Spain": ("- Develop a self-manageable hybrid renewable energy system\n"
                           "- Design a sustainable system with cost-effective components\n"
                           "- Test operation and maintenance under real conditions, which can be implemented in several locations."),

    "Energy Community, Portugal": ("- Taking advantage of endogenous sources of energy\n"
                           "- Energy self-sufficiency for the community, an ambition expressed by the municipality in response to global warming and the energy crisis\n"
                           "- Increase attractiveness and competitiveness of the region\n"
                           "- Rehabilitate old installations to create a hybrid renewable energy system.")
}

keys_figures_path = {
    "Irrigation System, Spain": "images/keysfigures_Irrigation%20System.JPG",
    "Fish Farm, Ireland": "images/keysfigures_Fisheries.JPG",
    "Port of Avilés, Spain": "images/keysfigures_Ports.JPG",
    "Energy Community, Portugal": "images/keysfigures_Portugal.JPG"
}

images_path = {
    "Irrigation System, Spain": "images/irrigationspain.jpg",
    "Fish Farm, Ireland": "images/ireland.jpg",
    "Port of Avilés, Spain": "images/portspain.jpg",
    "Energy Community, Portugal": "images/portugal.jpg"
}

time_series_path = {
    "Irrigation System, Spain": [
        "htmls/irrigation_time_series.html",
        "htmls/boxplot_weekday_Irrigation%20System.html",
        "htmls/Aggregated_time_serie_Irrigation%20System.html",
        "htmls/boxplot_day_Irrigation%20System.html",
        "htmls/time_serie_by_year_vs_doiIrrigation%20System.html",
        "htmls/histogram_Irrigation%20System.html",
        "htmls/time_serie_by_year_vs_monthIrrigation%20System.html",
        "htmls/boxplot_year_Irrigation%20System.html",
        "htmls/hurst_evolution_of_Irrigation%20System.html"
    ],
    "Fish Farm, Ireland": [
        "htmls/time_serie_Fisheries.html",
        "htmls/boxplot_weekday_Fisheries.html",
        "htmls/Aggregated_time_serie_Fisheries.html",
        "htmls/boxplot_day_Fisheries.html",
        "htmls/time_serie_by_year_vs_doiFisheries.html",
        "htmls/histogram_Fisheries.html",
        "htmls/time_serie_by_year_vs_monthFisheries.html",
        "htmls/boxplot_year_Fisheries.html",
        "htmls/hurst_evolution_of_Fisheries.html"
    ],
    "Port of Avilés, Spain": [
        "htmls/time_serie_Ports.html",
        "htmls/boxplot_weekday_Ports.html",
        "htmls/Aggregated_time_serie_Ports.html",
        "htmls/boxplot_day_Ports.html",
        "htmls/time_serie_by_year_vs_doiPorts.html",
        "htmls/histogram_Ports.html",
        "htmls/time_serie_by_year_vs_monthPorts.html",
        "htmls/boxplot_year_Ports.html",
        "htmls/hurst_evolution_of_Ports.html"
    ],
    "Energy Community, Portugal": [
        "htmls/time_serie_Portugal.html",
        "htmls/boxplot_weekday_Portugal.html",
        "htmls/Aggregated_time_serie_Portugal.html",
        "htmls/boxplot_day_Portugal.html",
        "htmls/time_serie_by_year_vs_doiPortugal.html",
        "htmls/histogram_Portugal.html",
        "htmls/time_serie_by_year_vs_monthPortugal.html",
        "htmls/boxplot_year_Portugal.html",
        "htmls/hurst_evolution_of_Portugal.html"
    ]
}

outliers_path = {
    "Irrigation System, Spain": ["htmls/outliers_analysis_Irrigation%20System.html"],
    "Fish Farm, Ireland": ["htmls/outliers_analysis_Fisheries.html"],
    "Port of Avilés, Spain": ["htmls/outliers_analysis_Ports.html"],
    "Energy Community, Portugal": ["htmls/outliers_analysis_Portugal.html"]
}

outliers_percentage_text = {
    "Irrigation System, Spain": "0.76%",
    "Fish Farm, Ireland": "5.94%",
    "Port of Avilés, Spain": "0.06%",
    "Energy Community, Portugal": "1.41%"}

outliers_number_text = {
    "Irrigation System, Spain": (
                                 "3601 kWh; 3767 kWh; 3878 kWh; 3915 kWh; 3865 kWh; 3712 kWh; 3634 kWh; 3620 kWh; 3678 kWh; 3642 kWh; 3670 kWh; 3647 kWh;<br>"
                                 "3656 kWh; 3642 kWh; 3617 kWh; 3658 kWh; 4090 kWh; 4090 kWh; 3988 kWh; 4157 kWh; 4124 kWh; 4011 kWh; 3927 kWh; 3753 kWh;<br>"
                                "3682 kWh; 3665 kWh; 3733 kWh; 3776 kWh; 3719 kWh; 3658 kWh; 3619 kWh; 3656 kWh; 3776 kWh; 3766 kWh; 3687 kWh; 3650 kWh;<br>"
                                "3832 kWh; 4143 kWh; 4130 kWh; 4231 kWh; 4193 kWh; 4024 kWh; 3953 kWh; 3878 kWh; 3815 kWh; 3727 kWh; 3683 kWh; 3683 kWh;<br>"
                                "3630 kWh; 3629 kWh; 3657 kWh; 3763 kWh; 3838 kWh; 3943 kWh; 4030 kWh; 3923 kWh; 3765 kWh; 3684 kWh; 3790 kWh; 3937 kWh;<br>"
                                "4025 kWh; 4299 kWh; 4164 kWh; 3958 kWh; 3800 kWh; 3732 kWh; 3744 kWh; 3844 kWh; 3814 kWh; 3687 kWh; 3792 kWh; 3819 kWh;<br>"
                                "3667 kWh; 3665 kWh; 3683 kWh; 3749 kWh; 3676 kWh; 3600 kWh; 3698 kWh; 3734 kWh; 3771 kWh; 3786 kWh; 3858 kWh; 3688 kWh;<br>"
                                "3756 kWh; 3700 kWh; 3626 kWh; 3716 kWh; 3711 kWh; 3659 kWh; 3685 kWh; 3619 kWh; 3678 kWh; 3771 kWh; 3840 kWh; 3825 kWh;<br>"
                                "3850 kWh; 3846 kWh; 3851 kWh; 3803 kWh; 3703 kWh; 3780 kWh; 3806 kWh; 3790 kWh; 3783 kWh; 3756 kWh; 3741 kWh; 3749 kWh;<br>"
                                "3756 kWh; 3840 kWh; 3884 kWh; 3848 kWh; 3825 kWh; 3816 kWh; 3758 kWh; 3768 kWh; 3967 kWh; 4147 kWh; 4149 kWh; 4221 kWh;<br>"
                                "4213 kWh; 4174 kWh; 3814 kWh; 3682 kWh; 3791 kWh; 3869 kWh; 3736 kWh; 3727 kWh; 3610 kWh; 3599 kWh; 3622 kWh; 3675 kWh;<br>"
                                "3693 kWh; 3721 kWh; 3642 kWh; 3663 kWh; 3715 kWh; 3794 kWh; 3742 kWh; 3737 kWh; 3723 kWh; 3621 kWh; 3772 kWh; 3857 kWh;<br>"
                                "3668 kWh; 3669 kWh; 3811 kWh; 3813 kWh; 3793 kWh; 3746 kWh; 3637 kWh; 3615 kWh; 3686 kWh; 3728 kWh; 3628 kWh; 3675 kWh;<br>"
                                "3779 kWh; 3717 kWh; 3737 kWh; 3721 kWh; 3648 kWh; 3630 kWh; 3728 kWh; 3703 kWh; 3684 kWh; 3832 kWh; 3794 kWh; 3755 kWh;<br>"
                                "3652 kWh; 3677 kWh; 3796 kWh; 3820 kWh; 3765 kWh; 3728 kWh; 3769 kWh; 3744 kWh; 3687 kWh; 3615 kWh; 3630 kWh; 3668 kWh;<br>"
                                "3674 kWh; 3654 kWh; 3602 kWh; 3755 kWh; 3847 kWh; 3822 kWh; 3792 kWh; 3876 kWh; 3925 kWh; 3726 kWh; 3639 kWh; 3629 kWh;<br>"
                                "3612 kWh; 3617 kWh; 3631 kWh; 3646 kWh; 3747 kWh; 3903 kWh; 3864 kWh; 3726 kWh; 3763 kWh; 3635 kWh; 3728 kWh; 3647 kWh;<br>"
                                "3623 kWh; 3625 kWh; 3737 kWh; 3653 kWh; 3667 kWh; 3601 kWh; 3639 kWh; 3623 kWh; 3642 kWh; 3815 kWh; 3870 kWh; 3884 kWh;<br>"
                                "3750 kWh; 3600 kWh; 3630 kWh; 3609 kWh; 3667 kWh; 3723 kWh; 3669 kWh; 3608 kWh; 3606 kWh; 3611 kWh; 3612 kWh; 3738 kWh;<br>"
                                "3928 kWh; 3747 kWh; 3626 kWh; 3838 kWh; 3611 kWh; 3612 kWh; 3659 kWh; 3643 kWh; 3607 kWh; 4056 kWh; 3756 kWh; 3807 kWh;<br>"
                                "3742 kWh; 3654 kWh; 4038 kWh; 4008 kWh; 4216 kWh; 4187 kWh; 4123 kWh; 3956 kWh; 3855 kWh; 3832 kWh; 3803 kWh; 3696 kWh;<br>"
                                "3630 kWh; 3726 kWh; 3855 kWh; 3684 kWh; 3598 kWh; 3674 kWh; 3743 kWh; 3683 kWh; 3641 kWh; 3875 kWh; 3920 kWh; 3966 kWh;<br>"
                                "3926 kWh; 3788 kWh; 3611 kWh;"),
    "Fish Farm, Ireland": ("782.75 kWh; 774.50 kWh;  756.75 kWh; ... 710.28 kWh; 706.52 kWh; 699.16 kWh. "),
    "Port of Avilés, Spain": ("629.736 kWh;<br> 573.871 kWh;<br> 548.077 kWh;<br> 545.046 kWh;<br> 554.986 kWh;<br> 547.332 kWh;<br> 549.863 kWh;<br> 540.988 kWh;<br> 553.821 kWh;<br> 555.12 kWh;<br> 540.413 kWh;<br> 559.365 kWh;<br> 548.759kWh."),
    "Energy Community, Portugal": ("37.57 kWh;     36.60 kWh;    31.11 kWh;    32.26 kWh;     29.42 kWh;     36.63 kWh;"
                                '33.60 kWh;  29.43 kWh;  31.31 kWh;  31.17 kWh;  32.78 kWh;  34.13 kWh;<br>'
                                '36.45 kWh;      29.10 kWh;     37.83 kWh;     36.36 kWh;     34.51 kWh;      29.55 kWh;'
                                '31.37 kWh;      31.67 kWh;     30.11 kWh;     29.97 kWh;     29.22 kWh;     34.25 kWh;<br>'
                                '36.19 kWh;     31.54 kWh;     29.45 kWh;      32.51 kWh;     29.40 kWh;     40.31 kWh;'
                                '33.18 kWh;     29.82 kWh;     29.10 kWh;     29.54 kWh;     34.66 kWh;     32.49 kWh;<br>'
                                '33.40 kWh;     29.85 kWh;      35.59 kWh;     30.61 kWh;     33.05 kWh;     39.39 kWh;'
                                '32.48 kWh;     32.51 kWh;     34.63 kWh;     33.30 kWh;     29.74 kWh;      30.13 kWh;<br>'
                                '29.48 kWh;     32.31 kWh;     34.44 kWh;      33.40 kWh;       34.73 kWh;      35.60 kWh;'
                                '32.75 kWh;     34.96 kWh;      33.46 kWh;      30.72 kWh;     31.36 kWh;      29.19 kWh;<br>'
                                '40.72 kWh;     43.68 kWh;      34.31 kWh;      31.11 kWh;      30.26 kWh;     32.68 kWh;'
                                '32.65 kWh;      35.30 kWh;       29.25 kWh;     31.26 kWh;      30.14 kWh;      31.97 kWh;<br>'
                                '33.37 kWh;     32.06 kWh;     30.47 kWh;     29.18 kWh;     30.15 kWh;      33.90 kWh;'
                                '29.32 kWh;      30.75 kWh;      30.03 kWh;     30.55 kWh;      29.05 kWh;      29.05 kWh;<br>'
                                '32.54 kWh;      33.34 kWh;      35.40 kWh;       30.55 kWh;      29.05 kWh;      29.05 kWh;'
                                '32.54 kWh;      33.34 kWh;      35.40 kWh;       33.88 kWh;     30.46 kWh;     30.38 kWh;<br>'
                                '29.52 kWh;     30.51 kWh;     31.07 kWh;     30.31 kWh;     31.56 kWh;      38.69 kWh;'
                                '37.70 kWh;   32.04 kWh;   33.22 kWh;   30.30 kWh;   37.72 kWh;    37.54 kWh;<br>'
                                '29.55 kWh;   29.97 kWh;   38.97 kWh;   37.45 kWh;   35.54 kWh;    30.44 kWh;'
                                '32.31 kWh;    32.62 kWh;   31.02 kWh;   30.87 kWh;   29.48 kWh;   30.09 kWh;<br>'
                                '35.28 kWh;   37.27 kWh;   32.48 kWh;    30.33 kWh;    29.27 kWh;    29.39 kWh;'
                                '29.20 kWh;   33.49 kWh;   29.07 kWh;   30.28 kWh;   41.52 kWh;   34.18 kWh;<br>'
                                '29.12 kWh;   30.72 kWh;   29.44 kWh;   29.35 kWh;   29.06 kWh;    29.97 kWh;'
                                '30.43 kWh;   35.70 kWh;   33.46 kWh;   34.40 kWh;   30.74 kWh;    36.66 kWh;<br>'
                                '31.53 kWh;   34.04 kWh;   40.57 kWh;   33.46 kWh;   29.39 kWh;   33.48 kWh;'
                                '35.67 kWh;   34.30 kWh;   30.63 kWh;    31.03 kWh;    30.36 kWh;   33.28 kWh;<br>'
                                '35.47 kWh;    34.40 kWh;     35.77 kWh;    36.66 kWh;     33.73 kWh;   36.00 kWh;'
                                '34.46 kWh;    31.64 kWh;   32.30 kWh;    30.07 kWh;   29.47 kWh;    29.75 kWh;<br>'
                                '41.94 kWh;   44.99 kWh;    35.33 kWh;   32.04 kWh;    31.17 kWh;   33.66 kWh;'
                                '33.62 kWh;    36.35 kWh;     30.13 kWh;   29.41 kWh;    29.72 kWh;    32.19 kWh;<br>'
                                '31.04 kWh;    32.93 kWh;   29.42 kWh;   34.37 kWh;   33.02 kWh;   31.38 kWh;'
                                '30.06 kWh;   31.05 kWh;    34.91 kWh;     30.19 kWh;    31.67 kWh;    30.93 kWh;<br>'
                                '29.19 kWh;   29.68 kWh;   29.42 kWh;    31.46 kWh;    29.92 kWh;    29.92 kWh;'
                                '33.51 kWh;    34.34 kWh;    36.46 kWh;     29.82 kWh;   34.90 kWh;   31.37 kWh;<br>'
                                '31.29 kWh;    30.41 kWh;   31.42 kWh;   32.00 kWh;   29.82 kWh;   29.68 kWh;'
                                '31.22 kWh;   32.50 kWh;    29.41 kWh;  40.63 kWh;  39.58 kWh;  33.65 kWh;<br>'
                                '34.89 kWh;  31.82 kWh;  30.28 kWh;  39.61 kWh;  39.42 kWh;  31.03 kWh;'
                                '29.41 kWh;  31.47 kWh;  40.92 kWh;  39.32 kWh;  37.32 kWh;  31.96 kWh;<br>'
                                '33.92 kWh;  34.25 kWh;  32.57 kWh;  29.89 kWh;  32.41 kWh;  30.37 kWh;'
                                '29.74 kWh;  30.95 kWh;  29.28 kWh;  29.28 kWh;   31.60 kWh;  29.89 kWh;<br>'
                                '37.05 kWh;  39.14 kWh;  34.11 kWh;   31.85 kWh;  30.73 kWh;   30.86 kWh;'
                                '30.66 kWh;  30.48 kWh;  29.31 kWh;  35.16 kWh;  30.52 kWh;  29.49 kWh;<br>'
                                '29.29 kWh;  31.80 kWh;  43.59 kWh;  35.89 kWh;  30.17 kWh;   30.58 kWh;'
                                '29.48 kWh;  30.11 kWh;  29.84 kWh;  30.16 kWh;  32.25 kWh;  29.39 kWh;<br>'
                                '30.92 kWh;  29.27 kWh;  30.41 kWh;  30.82 kWh;  30.51 kWh;   31.47 kWh;'
                                '31.95 kWh;  37.49 kWh;  35.14 kWh;  36.12 kWh;  29.16 kWh;  30.23 kWh;<br>'
                                '32.28 kWh;  38.49 kWh;  33.11 kWh;  35.74 kWh;  42.60 kWh;  35.13 kWh;'
                                '29.32 kWh;  30.86 kWh;  35.16 kWh;  37.46 kWh;  36.01 kWh;  32.16 kWh;<br>'
                                '30.05 kWh;  29.60 kWh; 32.58 kWh;  31.88 kWh; 34.94 kWh; 37.24 kWh;'
                                '36.12 kWh;  37.56 kWh;  38.50 kWh;    35.42 kWh; 37.80 kWh;   36.18 kWh;<br>'
                                '33.22 kWh; 30.34 kWh;   33.91 kWh;   30.37 kWh;  31.57 kWh; 30.95 kWh;'
                                '31.24 kWh;  44.04 kWh; 47.23 kWh;   37.10 kWh;  33.64 kWh;  32.73 kWh;<br>'
                                '35.34 kWh; 29.88 kWh; 35.31 kWh;  29.47 kWh;  30.37 kWh;  38.17 kWh;'
                                '31.63 kWh; 29.43 kWh;   29.61 kWh;   30.88 kWh;   31.21 kWh;   33.80 kWh;<br>'
                                '29.38 kWh; 29.34 kWh; 30.04 kWh;   30.36 kWh;   32.59 kWh;   34.58 kWh;'
                                '30.89 kWh; 29.40 kWh; 36.09 kWh; 34.67 kWh; 32.95 kWh; 31.56 kWh;<br>'
                                '29.71 kWh; 29.11 kWh;   32.60 kWh;  36.66 kWh;   29.20 kWh; 29.17 kWh;'
                                '29.25 kWh; 31.70 kWh;   33.25 kWh;  32.48 kWh; 29.83 kWh; 30.65 kWh;<br>'
                                '29.47 kWh; 31.17 kWh; 30.89 kWh;  33.03 kWh;  31.41 kWh;  31.41 kWh;'
                                '35.19 kWh;   29.90 kWh; 36.05 kWh;   38.28 kWh;    29.25 kWh; 29.74 kWh;<br>'
                                '29.59 kWh;  29.15 kWh;  31.31 kWh;  29.38 kWh;  36.64 kWh;  32.94 kWh;'
                                '29.41 kWh;  32.85 kWh;   29.39 kWh;  31.93 kWh;  33.00 kWh;  30.28 kWh.<br>')
}

outilers_number = {
    "Irrigation System, Spain": "267",
    "Fish Farm, Ireland": "2,084",
    "Port of Avilés, Spain": "13",
    "Energy Community, Portugal": "372"}

correlation_path = {
    "Irrigation System, Spain": [
        "htmls/pearson_correlation_Irrigation System.html",
        "htmls/spearman_correlation_Irrigation System.html",
        "htmls/biserial_day_night_Irrigation_System.html",
        "htmls/biserial_weekday_vs_weekend_Irrigation_System.html",
        "htmls/biserial_Boolean_precipitation_Irrigation_System.html"
    ],

    "Fish Farm, Ireland": [
        "htmls/pearson_correlation_Fisheries.html",
        "htmls/spearman_correlation_Fisheries.html",
        "htmls/biserial_day_night_Fisheries.html",
        "htmls/biserial_weekday_vs_weekend_Fisheries.html"
    ],

    "Port of Avilés, Spain": [
        "htmls/pearson_correlation_Ports.html",
        "htmls/spearman_correlation_Ports.html",
        "htmls/biserial_day_night_Ports.html",
        "htmls/biserial_weekday_vs_weekend_Ports.html"
    ],

    "Energy Community, Portugal": [
        "htmls/pearson_correlation_Portugal.html",
        "htmls/spearman_correlation_Portugal.html",
        "htmls/biserial_day_night_Portugal.html",
        "htmls/biserial_weekday_vs_weekend_Portugal.html"
    ]
}


correlation_labels = {
    "Irrigation System, Spain":
        ["📈 Pearson Correlation (Numerical Variables)",
        "📈 Spearman Correlation (Ordinal/Discrete Variables)",
        "📊 Biserial Correlation: Time of the day (0=Night and 1=Day)",
        "📊 Biserial Correlation: Days of the week (0=Weekend and 1=Weekday)",
        "📊 Biserial Correlation: Boolean precipitation (0=No, 1=Yes)"],
    "Fish Farm, Ireland":
        ["📈 Pearson Correlation (Numerical Variables)",
         "📈 Spearman Correlation (Ordinal/Discrete Variables)",
         "📊 Biserial Correlation: Time of the day (0=Night and 1=Day)",
         "📊 Biserial Correlation: Days of the week (0=Weekend and 1=Weekday)"
         ],
    "Port of Avilés, Spain":
        ["📈 Pearson Correlation (Numerical Variables)",
         "📈 Spearman Correlation (Ordinal/Discrete Variables)",
         "📊 Biserial Correlation: Time of the day (0=Night and 1=Day)",
         "📊 Biserial Correlation: Days of the week (0=Weekend and 1=Weekday)"],
    "Energy Community, Portugal":
        ["📈 Pearson Correlation (Numerical Variables)",
         "📈 Spearman Correlation (Ordinal/Discrete Variables)",
         "📊 Biserial Correlation: Time of the day (0=Night and 1=Day)",
         "📊 Biserial Correlation: Days of the week (0=Weekend and 1=Weekday)"],
}

correlation_text = {
    "Irrigation System, Spain": [(
            "This heatmap shows **Pearson correlation** between numerical variables, useful for linear relationships.\n\n"
            "**Variables analyzed:**\n"
            "- Maximum Temperature\n"
            "- Minimum Temperature\n"
            "- Mean Temperature\n"
            "- Radiation (MJ/m²/day)\n"
            "- ETo (Evapotranspiration)\n"
            "- Max Wind speed (m/s)\n"
            "- Mean Wind speed (m/s)\n"
            "- T-1, T-2 and T-3 (previous time steps)"),
        ("This heatmap displays **Spearman correlation**, ideal for ordinal or non-linear monotonic relationships.\n\n"
            "**Variables analyzed:**\n"
            "- Day of the Year (DOY)\n"
            "- Month\n"
            "- Period (Tariff Period)\n"
            "- Citrus Area (% of total area)\n"
            "- Cotton Area (% of total area)\n"
            "- Potatoes Area (% of total area)\n"
            "- Wheat Area (% of total area)\n"
            "- Sunflower Area (% of total area)\n"
            "- Hours of the Day\n"
            "- Hours of the Year"),
        ("This boxplot shows the impact of **daytime vs nighttime** on energy consumption.\n\n"
            "**Variable analyzed:**\n"
            "- Time of Day (0 = Night, 1 = Day)"),
        ("This boxplot compares **weekdays vs weekends** for energy consumption behavior.\n\n"
            "**Variable analyzed:**\n"
            "- Day Type (0 = Weekend, 1 = Weekday)"),
        ("This boxplot analyzes the **point-biserial correlation** between a binary variable and energy consumption.\n\n"
            "**Variable analyzed:**\n"
            "- Boolean Precipitation (0 = No, 1 = Yes)")],
    "Fish Farm, Ireland": [(
            "This heatmap shows **Pearson correlation** between numerical variables, useful for linear relationships.\n\n"
            "**Variables analyzed:**\n"
            "- T-1, T-2, T-3, T-4, T-5, T-6 and T-7 (previous time steps)"),
        ("This heatmap displays **Spearman correlation**, ideal for ordinal or non-linear monotonic relationships.\n\n"
            "**Variables analyzed:**\n"
            "- Day of the Year (DOY)\n"
            "- Month\n"
            "- Hours of the Year\n"
            "- Hours of the Day"),
        ("This boxplot shows the impact of **daytime vs nighttime** on energy consumption.\n\n"
            "**Variable analyzed:**\n"
            "- Time of Day (0 = Night, 1 = Day)"),
        ("This boxplot compares **weekdays vs weekends** for energy consumption behavior.\n\n"
            "**Variable analyzed:**\n"
            "- Day Type (0 = Weekend, 1 = Weekday)")],
    "Port of Avilés, Spain": [(
            "This heatmap shows **Pearson correlation** between numerical variables, useful for linear relationships.\n\n"
            "**Variables analyzed:**\n"
            "- T-1, T-2, T-3, T-4, T-5, T-6 and T-7 (previous time steps)"),
        ("This heatmap displays **Spearman correlation**, ideal for ordinal or non-linear monotonic relationships.\n\n"
            "**Variables analyzed:**\n"
            "- Day of the Year (DOY)\n"
            "- Month\n"
            "- Hours of the Year\n"
            "- Hours of the Day"),
        ("This boxplot shows the impact of **daytime vs nighttime** on energy consumption.\n\n"
            "**Variable analyzed:**\n"
            "- Time of Day (0 = Night, 1 = Day)"),
        ("This boxplot compares **weekdays vs weekends** for energy consumption behavior.\n\n"
            "**Variable analyzed:**\n"
            "- Day Type (0 = Weekend, 1 = Weekday)")],
    "Energy Community, Portugal": [(
            "This heatmap shows **Pearson correlation** between numerical variables, useful for linear relationships.\n\n"
            "**Variables analyzed:**\n"
            "- Maximum Temperature\n"
            "- Minimum Temperature\n"
            "- Maximum Humidity\n"
            "- Mean Humidity\n"
            "- Minimum Humidity\n"
            "- Maximum Wind Speed\n"
            "- Mean Wind Speed\n"
            "- Minimum Wind Speed\n"
            "- Maximum Pressure\n"
            "- Mean Pressure\n"
            "- Minimum Pressure\n"
            "- ETo (Evapotranspiration)\n"
            "- T-1, T-2 and T-3 (previous time steps)"),
        ("This heatmap displays **Spearman correlation**, ideal for ordinal or non-linear monotonic relationships.\n\n"
            "**Variables analyzed:**\n"
            "- Day of the Year (DOY)\n"
            "- Month"),
        ("This boxplot shows the impact of **daytime vs nighttime** on energy consumption.\n\n"
            "**Variable analyzed:**\n"
            "- Time of Day (0 = Night, 1 = Day)"),
        ("This boxplot compares **weekdays vs weekends** for energy consumption behavior.\n\n"
            "**Variable analyzed:**\n"
            "- Day Type (0 = Weekend, 1 = Weekday)")]
}

fuzzy_logic_path = {
    "Irrigation System, Spain": ["htmls/fuzzy_surfaces_Irrigation_System.html"],
    "Fish Farm, Ireland": ["htmls/fuzzy_surfaces_Fisheries.html"],
    "Port of Avilés, Spain": ["htmls/fuzzy_surfaces_Ports.html"],
    "Energy Community, Portugal": ["htmls/fuzzy_surfaces_Portugal.html"]
}


fuzzylogic_text = {
    "Irrigation System, Spain": (
                                 "- Minimum Temperature (ºC): 120\n"
                                 "- Maximum Wind Speed (m/s): 120\n"
                                 "- Radiation (MJ/m2day): 100\n"
                                 "- Mean Temperature (ºC): 100\n"
                                 "- Maximum Temperature (ºC): 80\n"
                                 "- Day vs. Night: 80\n"
                                 "- T-2: 60\n"
                                 "- Mean Wind Speed (m/s): 60\n"
                                 "- Boolean Precipitation (0-1): 60\n"),
    "Fish Farm, Ireland": (
                            "- T-5: 100\n"
                            "- T-6: 100\n"
                            "- T-4: 80\n"
                            "- T-7: 80\n"
                            "- T-3: 60\n"
                            "- Day of Year (DOY): 60\n"
                            "- T-2: 40\n"
                            "- Hours of Year: 40\n"
                            "- Month: 40\n"),
    "Port of Avilés, Spain": (
                            "- T-3: 100\n"
                            "- T-4: 100\n"
                            "- T-2: 80\n"
                            "- T-6: 80\n"
                            "- Hours of Day: 60\n"
                            "- T-5: 60\n"),
    "Energy Community, Portugal": (
                                 "- Mean Pressure (HPa): 140\n"
                                 "- Maximum Temperature (ºC): 120\n"
                                 "- Minimum Temperature (ºC): 120\n"
                                 "- T-3: 100\n"
                                 "- Mean Humidity (%): 80\n"
                                 "- Maximum Wind Speed (m/s): 80\n"
                                 "- T-2: 60\n"
                                 "- Month of Year: 60\n"
                                 "- Mean Temperature (ºC): 60\n")
}

inputs_text = {
    "Irrigation System, Spain": ("After a comprehensive analysis of all results obtained from the different statistical approaches, the following 12 variables were selected as model input variables:\n\n"
                                 "- 1) T-1, T-2 and T-3\n"
                                 "- 4) Radiation\n"
                                 "- 5) ETo (Evapotranspiration)\n"
                                 "- 6) Mean Temperature\n"
                                 "- 7) Maximum Temperature\n"
                                 "- 8) Minimum Temperature\n"
                                 "- 9) Day of the Year (DOY)\n"
                                 "- 10) Maximum Wind Speed\n"
                                 "- 11) Day vs. Night\n" 
                                 "- 12) Boolean Precipitation\n\n"
                                 "The remaining 14 candidate input variables were discarded based on this statistical analysis."),
    "Fish Farm, Ireland": ("After a comprehensive analysis of all results obtained from the different statistical approaches, the following 6 variables were selected as model input variables:\n\n"
                                 "- 1) T-1, T-2, T-3, T-4 and T-5\n"
                                 "- 6) Hours of Year\n\n"
                                 "The remaining  potential input variables were discarded based on this statistical analysis."),
    "Port of Avilés, Spain": ("After a comprehensive analysis of all results obtained from the different statistical approaches, the following 6 variables were selected as model input variables:\n\n"
                                 "- 1) T-1, T-2, T-3 and T-4\n"
                                 "- 5) Day vs. Night\n"
                                 "- 6) Weekend vs. Weekday\n\n"
                                 "The remaining  potential input variables were discarded based on this statistical analysis."),
    "Energy Community, Portugal": ("After a comprehensive analysis of all results obtained from the different statistical approaches, the following 6 variables were selected as model input variables:\n\n"
                                 "- 1) Maximum Temperature\n"
                                 "- 2) Minimum Temperature\n"
                                 "- 3) Maximum Humidity\n"
                                 "- 4) T-1, T-2 and T-3\n\n"
                                 "The remaining 14 candidate input variables were discarded based on this statistical analysis.")
}

html_paths = {
    "Time Series Analysis": time_series_path,
    "Outliers Analysis": outliers_path,
    "Correlation Analysis": correlation_path,
    "Fuzzy Logic Analysis": fuzzy_logic_path,
    "Selected Input Variables": inputs_text
}

model_options_by_site = {
    "Irrigation System, Spain": [
        "Hyperparameters",
        "Energy Demand Forecasting"
    ],
    "Fish Farm, Ireland": [
        "Hyperparameters",
        "Energy Demand Forecasting"
    ],
    "Port of Avilés, Spain": [
        "Hyperparameters",
        "Energy Demand Forecasting"
    ],
    "Energy Community, Portugal": [
        "Hyperparameters",
        "Energy Demand Forecasting"
    ]
}

# Información sobre hiperparámetros por sitio
hyperparameters_text = {
    "Irrigation System, Spain":
        (
        "- Input variables: 12 selected variables\n"
        "- Output variable: Energy demand (kWh)\n"
        "- Data preprocessing: Normalization and scaling\n"
        "- Learning rate: CustemSchedule\n"
        "- Batch size:  96\n"
        "- Sequence length: 168\n"
        "- Optimizer: Adam\n"
        "- Dropout rate: 0.1\n"
        "- Loss function: MSE (Mean Squared Error)\n"
        "- Early stopping, Patience: 10\n"
        "- Validation split: 0.15\n"
        "- Training epochs: 350\n"
         "- Teacher Forcing: Enabled\n"
        "- Performance metrics: MAE, R2\n"),

    "Fish Farm, Ireland": (
        "- Input variables: 6 selected variables\n"
        "- Output variable: Energy demand (kWh)\n"
        "- Learning rate: CustemSchedule\n"
        "- Batch size: 96\n"
        "- Sequence length: 168\n"
        "- Epochs: 350\n"
        "- Optimizer: Adam",
        "- Dropout rate: 0.1\n"
        "- Loss function: MSE (Mean Squared Error)\n"
        "- Early stopping, Patience: 10\n"
        "- Validation split: 0.15\n"
        "- Training epochs: 350\n"
        "- Teacher Forcing: Enabled\n"
        "- Performance metrics: MAE, R2\n"
    ),
    "Port of Avilés, Spain":
        (
            "- Input variables: 6 selected variables\n"
            "- Output variable: Energy demand (kWh)\n"
            "- Learning rate: CustemSchedule\n"
            "- Batch size: 128\n"
            "- Sequence length: 168\n"
            "- Epochs: 350\n"
            "- Optimizer: Adam",
            "- Dropout rate: 0.1\n"
            "- Loss function: MSE (Mean Squared Error)\n"
            "- Early stopping, Patience: 10\n"
            "- Validation split: 0.15\n"
            "- Training epochs: 350\n"
            "- Teacher Forcing: Enabled\n"
            "- Performance metrics: MAE, R2\n"
        ),
    "Energy Community, Portugal":
        (
            "- Input variables: 6 selected variables\n"
            "- Output variable: Energy demand (kWh)\n"
            "- Learning rate: CustemSchedule\n"
            "- Batch size: 96\n"
            "- Sequence length: 168\n"
            "- Epochs: 350\n"
            "- Optimizer: Adam",
            "- Dropout rate: 0.1\n"
            "- Loss function: MSE (Mean Squared Error)\n"
            "- Early stopping, Patience: 10\n"
            "- Validation split: 0.15\n"
            "- Training epochs: 350\n"
            "- Teacher Forcing: Enabled\n"
            "- Performance metrics: MAE, R2\n"
        )
}

# Información sobre pronóstico energético por sitio
results_text = {
    "Irrigation System, Spain": "📈 **Metrics**:\n\n"
                          "- R2: 99.42%\n"
                          "- RMSE: 0.047\n"
                          "- MAE: 40.78 kWh\n",
    "Fish Farm, Ireland": "📈 **Metrics**:\n\n"
                          "- R2: 97.91%\n"
                          "- RMSE: 0.149\n"
                          "- MAE: 23.04 kWh\n",
    "Port of Avilés, Spain": "📈 **Metrics**:\n\n"
                          "- R2: 98.67%\n"
                          "- RMSE: 0.072\n"
                          "- MAE: 6.64 kWh\n",
    "Energy Community, Portugal": "📈 **Metrics**:\n\n"
                          "- R2: 98.58%\n"
                          "- RMSE: 0.083\n"
                          "- MAE: 0.44 kWh\n"
}
results_r2_path = {
    "Irrigation System, Spain": "images/r2_Irrigation System.png",
    "Fish Farm, Ireland": "images/r2_Fisheries.png",
    "Port of Avilés, Spain": "images/r2_Ports.png",
    "Energy Community, Portugal": "images/r2_Portugal.png"
}

results_pred_path = {
    "Irrigation System, Spain": "images/combined_Irrigation System2.png",
    "Fish Farm, Ireland": "images/combined_Fisheries2.png",
    "Port of Avilés, Spain": "images/combined_Ports2.png",
    "Energy Community, Portugal": "images/combined_Portugal2.png"
}

results_pred_path2 = {
    "Irrigation System, Spain": "images/combined_Irrigation System.png",
    "Fish Farm, Ireland": "images/combined_Fisheries.png",
    "Port of Avilés, Spain": "images/combined_Ports.png",
    "Energy Community, Portugal": "images/combined_Portugal.png"
}

results_pred_path3 = {
    "Irrigation System, Spain": "images/combined_Irrigation System3.png",
    "Fish Farm, Ireland": "images/combined_Fisheries3.png",
    "Port of Avilés, Spain": "images/combined_Ports3.png",
    "Energy Community, Portugal": "images/combined_Portugal3.png"
}

results_pred_path4 = {
    "Irrigation System, Spain": "images/combined_Irrigation System4.png",
    "Fish Farm, Ireland": "images/combined_Fisheries4.png",
    "Port of Avilés, Spain": "images/combined_Ports4.png",
    "Energy Community, Portugal": "images/combined_Portugal4.png"
}

results_loss_path = {
    "Irrigation System, Spain": "images/training_loss_Irrigation System.png",
    "Fish Farm, Ireland": "images/training_loss_Fisheries.png",
    "Port of Avilés, Spain": "images/training_loss_Ports.png",
    "Energy Community, Portugal": "images/training_loss_Portugal.png"
}

hyperparameters_code_text = {
    "Irrigation System, Spain":
        ("""
        "# Hyperparameters
        d_model = 256
        dff = 1024
        num_heads = 4
        num_layers = 2
        input_seq_length = 12
        output_seq_length = 168
        dropout_rate = 0.1
        learning_rate = CustomSchedule(d_model)
        optimizer = Adam(learning_rate) #, beta_1=0.9, beta_2=0.98, epsilon=1e-9)
        BATCH_SIZE_TRAIN = 96"""),

    "Fish Farm, Ireland":
        ("""
        "# Hyperparameters
        d_model = 256
        dff = 1024
        num_heads = 4
        num_layers = 2
        input_seq_length = 6
        output_seq_length = 168
        dropout_rate = 0.1
        learning_rate = CustomSchedule(d_model)
        optimizer = Adam(learning_rate) #, beta_1=0.9, beta_2=0.98, epsilon=1e-9)
        BATCH_SIZE_TRAIN = 96"""),
    "Port of Avilés, Spain":
        ("""
        "# Hyperparameters
        d_model = 256
        dff = 1024
        num_heads = 4
        num_layers = 2
        input_seq_length = 6
        output_seq_length = 168
        dropout_rate = 0.1
        learning_rate = CustomSchedule(d_model)
        optimizer = Adam(learning_rate) #, beta_1=0.9, beta_2=0.98, epsilon=1e-9)
        BATCH_SIZE_TRAIN = 128"""),
    "Energy Community, Portugal":
        ("""
        "# Hyperparameters
        d_model = 256
        dff = 1024
        num_heads = 4
        num_layers = 2
        input_seq_length = 6
        output_seq_length = 168
        dropout_rate = 0.1
        learning_rate = CustomSchedule(d_model)
        optimizer = Adam(learning_rate) #, beta_1=0.9, beta_2=0.98, epsilon=1e-9)
        BATCH_SIZE_TRAIN = 96""")
}

# --- Sidebar ---
st.sidebar.title("Navigation")
st.sidebar.markdown("Use the menu below to navigate the results.")

# Sidebar selections
selected_site = st.sidebar.selectbox("Select Pilot Site", [
    "Irrigation System, Spain",
    "Fish Farm, Ireland",
    "Port of Avilés, Spain",
    "Energy Community, Portugal"
])
selected_analysis = st.sidebar.selectbox("Select Data Analysis", [
    "Time Series Analysis",
    "Outliers Analysis",
    "Correlation Analysis",
    "Fuzzy Logic Analysis",
    "Selected Input Variables"
])
selected_model = st.sidebar.selectbox("Forecast Model Results", model_options_by_site[selected_site])

# --- Main Content ---
img_path = Image.open("images/InterregLogo.png")
st.image(img_path, use_column_width=False)
st.title("HY4RES: Hybrid Solutions For Renewable Energy Systems 🌱")
st.header("WP 2.1: Forecasting Models for predicting real-time energy demand for different users (Agriculture, Aquaculture, Ports & Communities).")
st.subheader(f"Results: {selected_site}")


# --- Select the Tab Visualization ---
tab1, tab2, tab3, tab4 = st.tabs(["🧠 Forecast Model Insights", "📍 Pilot Site Information", "📊 Data Analysis", "📉 TNN Model Results"])

# Mostrar HTMLs Data Analysis
with tab1:
    st.subheader("🧾 **Introduction**:\n\n")
    st.write(
              "WP2.1 has developed a set of methodologies for real-time energy demand forecasting across the four sectors of the HY4RES project based on data analytics and artificial intelligence techniques:\n"
                "- Agriculture: Irrigation System, Seville, Spain\n"
                "- Aquaculture: Killybegs Seafoods, Ireland\n"
                "- Ports: Port of Aviles, Spain\n"
                "- Communities: Marruge, Portugal\n\n"
                "The performance of the latest AI techniques was evaluated in four sectors: artificial neural networks; deep learning techniques; support vector regression; and model predictive control. A collaborative approach to AI model development was adopted to generate the highest-performing model in each sector. These models learn from historical energy consumption data and other factors, such as weather forecasts, in order to provide a real-time estimate of demand for the coming days. The proposed model integrates Transformer Neural Networks (TNNs) with fuzzy logic and correlation matrices to improve prediction accuracy. Using real historical data from 2020 to 2023, the model employs a sequence-by-sequence structure to capture complex temporal dependencies. Input variables include weather factors, energy prices, crop distribution, and historical energy consumption patterns. The model has considered:\n"
                "- Time horizon: 7 days (168 hours)\n"
                "- Prediction frequency: hourly\n"
                "- -------------------------\n")

    st.subheader("🧬 **TNN Architecture**:\n\n")
    st.write("Our prediction model is based on the original Transformer architecture proposed by Vaswani. The Transformer Neural Network (TNN) follows a recursive encoder-decoder structure, incorporating multi-head attention mechanisms and positional encoding while utilizing teacher forcing during training.\n")
    img_path = Image.open("images/TransformerArchitecture.png")
    st.image(img_path, use_column_width=True)
    st.write("- a) Encoder Layer\n"
             "- b) Decoder Layer\n"
             "- c) Feed-forward neural network\n"
             "- d) Multi-head attention mechanism\n"
             "- e) Scaled Dot-Product Attention\n")

    st.write("- -------------------------\n")

    st.subheader("🤖 **Model Framework Flowchart**:\n\n")
    img_path = Image.open("images/Flowchart.png")
    st.image(img_path, use_column_width=True)
    st.write("- 1) Data Pre-procesing and Data Analysis\n"
             "- 2) Training Step\n"
             "- 3) Testing Step\n")
    st.write("- -------------------------\n")

with tab2:
    st.subheader(f"Selected Pilot Site: {selected_site}")
    st.markdown(pilot_text[selected_site], unsafe_allow_html=True)

    st.subheader('🔓 Keys Figures:')
    img_path = Image.open(keys_figures_path[selected_site])
    st.image(img_path, use_column_width=True)

    st.subheader('🎯 Objectives:')
    st.markdown(objectives_pilot_text[selected_site], unsafe_allow_html=True)
    img_path = Image.open(images_path[selected_site])
    st.image(img_path, use_column_width=True)

with tab3:
    st.subheader(f"Data Analysis Type: {selected_analysis}")
    try:
        html_files = html_paths[selected_analysis][selected_site]

        if selected_analysis == "Outliers Analysis":
            for html_path in html_files:
                if os.path.exists(html_path):
                    with open(html_path, "r", encoding="utf-8") as f:
                        raw_html = f.read()
                    # Mostrar directamente en grande, sin escalar ni expander
                    components.html(raw_html, width=1200, height=480, scrolling=True)
                else:
                    st.error(f"File not found: {html_path}")
            st.subheader("Percentage of Outliers:")
            st.markdown(outliers_percentage_text[selected_site], unsafe_allow_html=True)
            st.write("- -------------------------\n")
            st.subheader(f" {outilers_number[selected_site]} Outliers Detected:")
            st.markdown(outliers_number_text[selected_site], unsafe_allow_html=True)

        elif selected_analysis == "Fuzzy Logic Analysis":
            for html_path in html_files:
                if os.path.exists(html_path):
                    with open(html_path, "r", encoding="utf-8") as f:
                        raw_html = f.read()
                    # Mostrar directamente en grande, sin escalar ni expander
                    components.html(raw_html, width=1200, height=600, scrolling=True)
                else:
                    st.error(f"File not found: {html_path}")
            st.subheader("Most influential variables in 20 executions:")
            st.markdown(fuzzylogic_text[selected_site], unsafe_allow_html=True)

        elif selected_analysis == "Correlation Analysis":
            site_labels = correlation_labels.get(selected_site, [])
            site_descriptions = correlation_text.get(selected_site, [])

            for i, html_path in enumerate(html_files):
                if os.path.exists(html_path):
                    label = site_labels[i] if i < len(site_labels) else f"Chart {i + 1}"
                    description = site_descriptions[i] if i < len(site_descriptions) else "No description available."

                    st.subheader(label)

                    with open(html_path, "r", encoding="utf-8") as f:
                        raw_html = f.read()

                    scaled_height = 420 if i < 2 else 550
                    scaled_html = f"""
                                <div style="transform: scale(0.85); transform-origin: top center; width: fit-content;">
                                    {raw_html}
                                </div>
                                """
                    components.html(scaled_html, height=scaled_height, scrolling=True)

                    st.markdown(description)

                else:
                    st.error(f"File not found: {html_path}")

        elif selected_analysis == "Time Series Analysis":
            for i in range(0, len(html_files), 3):
                group = html_files[i:i+3]
                cols = st.columns([1, 1, 1])  # 3 columnas por fila

                for j, html_path in enumerate(group):
                    with cols[j]:
                        if os.path.exists(html_path):
                            with open(html_path, "r", encoding="utf-8") as f:
                                raw_html = f.read()
                                # Mostrar en escala reducida
                                scaled_html = f"""
                                <div style="transform: scale(0.6); transform-origin: top left; width: fit-content;">
                                    {raw_html}
                                </div>
                                """
                                components.html(scaled_html, width=400, height=300, scrolling=False)
                            # Expander con versión completa
                            with st.expander("🔍 Expand to view full-size chart"):
                                components.html(raw_html, width=800, height=600, scrolling=True)
                        else:
                            st.error(f"File not found: {html_path}")

        else:
            st.subheader("Selected Input Variables:")
            st.markdown(inputs_text[selected_site], unsafe_allow_html=True)
            st.write("- -------------------------\n")

    except KeyError:
        st.warning("No HTMLs available for this selection.")

with tab4:
    st.subheader(f"{selected_model}")
    if selected_model == "Hyperparameters":
        st.markdown(hyperparameters_text[selected_site], unsafe_allow_html=True)
        st.write("This section provides insights into the selected model's hyperparameters and energy demand forecasting results.")
        with st.expander("📄 Code"):
            st.code(hyperparameters_code_text[selected_site], language="python")
        st.write("- -------------------------\n")
        st.subheader("Model architecture: Transformer Neural Network (TNN)")
        st.write("The Transformer Neural Network (TNN) is a powerful architecture designed for sequence-to-sequence tasks, leveraging self-attention mechanisms to capture complex temporal dependencies in time series data.\n"
                 "The proposed Transformer Neural Network (TNN) model was developed using an Intel Core i7-1195G7 CPU @ 2.90 GHz and 16 GB of RAM computer, built using TensorFlow in Python 3.10.0 using PyCharm software.\n")
        st.write(
                 "- Encoder-Decoder Architecture\n"
                 "- Multi-Head Attention Mechanism\n"
                 "- Positional Encoding: Sine and Cosine functions\n"
                 "- Teacher Forcing during Training\n"
                 "- Encoder stack: 2\n"
                 "- Decoder stack: 2\n"
                 "- Number of heads/attention layers: 4\n"
                 "- Dimensionality of the model: 256\n"
                 "- Dimensionality of the inner layer: 1024\n"
                 )
        with st.expander("📄 Requeriments"):
            st.code("""
        # Requeriments.txt
        numpy~=1.26.4
        pandas~=1.5.3
        matplotlib~=3.9.0
        ipython~=8.27.0
        sympy~=1.13.1
        tabulate~=0.9.0
        tensorflow~=2.10.0
        keras~=2.10.0
        sklearn~=0.0
        scikit-learn~=1.6.1
        streamlit~=1.27.0
        seaborn~=0.13.2
        scipy~=1.13.1
        torch~=2.5.0
        icecream~=2.1.3
        joblib~=1.4.2
        tqdm~=4.67.1
        cffi~=1.17.1
        defusedxml~=0.7.1
        typing_extensions~=4.12.2
        future~=1.0.0
        Pillow~=9.5.0
        pip~=24.3.1
        attrs~=24.2.0
        wheel~=0.43.0
        tornado~=6.4.1
        Jinja2~=3.0.3
        pytz~=2024.2
        pytest~=8.3.3
        setuptools~=75.8.0
        overrides~=7.7.0
        openpyxl~=3.1.5
        fsspec~=2024.6.1
        pyarrow~=17.0.0
        MarkupSafe~=3.0.2
        python-dateutil~=2.9.0.post0
        tzdata~=2024.2
        six~=1.17.0
        contourpy~=1.3.0
        fonttools~=4.55.3
        pyparsing~=3.2.1
        importlib_resources~=6.5.2
        cycler~=0.12.1
        packaging~=23.2
        ipykernel~=6.29.5
        kiwisolver~=1.4.7
        astral~=3.2
        plotly~=6.0.0
        pymannkendall~=1.4.3
        statsmodels~=0.14.4
        fpdf~=1.7.2
            """, language="python")

    elif selected_model == "Energy Demand Forecasting":

        col1, col2 = st.columns(2)
        with col1:
            st.image(Image.open(results_pred_path[selected_site]).resize((700, 450)))
        with col2:
            st.image(Image.open(results_pred_path2[selected_site]).resize((700, 450)))

        col1, col2 = st.columns(2)
        with col1:
            st.image(Image.open(results_pred_path3[selected_site]).resize((700, 450)))
        with col2:
            st.image(Image.open(results_pred_path4[selected_site]).resize((700, 450)))

        # col3 = st.columns(1)
        # with col3:
        #     st.image(Image.open(results_loss_path[selected_site]).resize((600, 300)))

        # st.markdown(results_text[selected_site], unsafe_allow_html=True)
        st.write("- -------------------------\n")

        with st.expander("📄 Code"):
            st.code("""
            Epoch 350, MSE_Loss_Train: 0.0005448752781376243, R2_Train: 0.9985947608947754, MAE_Train: 0.013299953192472458, 
            MSE_Loss_Val: 0.0011772210709750652, R2_Val: 0.9970002770423889, MAE_Val: 0.023894090205430984
            Model: "transformer_model"
            _________________________________________________________________
             Layer (type)                Output Shape              Param #   
            =================================================================
             encoder (Encoder)           multiple                  1580032   
            
             decoder (Decoder)           multiple                  2107392   
            
             dense_34 (Dense)            multiple                  257       
            
            =================================================================
            Total params: 3,687,681
            Trainable params: 3,687,681
            Non-trainable params: 0
            _________________________________________________________________
            Layer: encoder, Parameters: 1580032
            Layer: decoder, Parameters: 2107392
            Layer: dense_34, Parameters: 257
            """, language="python")

        img_path = Image.open(results_loss_path[selected_site])
        st.image(img_path, use_column_width=True, width=700)

        img_path = Image.open(results_r2_path[selected_site])
        st.image(img_path, use_column_width=True, width=700)
