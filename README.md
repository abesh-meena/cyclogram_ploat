# Enhanced Gait Cyclogram Analyzer

**Enhanced Gait Cyclogram Analyzer** is an interactive Python-based tool for biomechanical gait analysis. It visualizes human walking data using joint angles and overlays it with computed zones of ZMP (Zero Moment Point), COM (Center of Mass), and Stability Zones to help assess dynamic balance and movement safety.

## 🚀 Features

- Visualize joint angle relationships as cyclograms.
- Annotate gait phases: **Stance Phase** (weight bearing) and **Swing Phase** (limb advancement).
- Compute and display:
  - **ZMP Area**: Ground reaction boundaries.
  - **COM Area**: Body mass trajectory zone.
  - **Stability Zone**: Safe movement region.
- Compare across multiple subjects.
- Export and analyze gait data.
- Interactive UI with dropdowns and toggles for flexible exploration.

## 📊 Data Summary

- **Activity Type**: Walking
- **Total Data Points**: 300
- **Stance Phase**: 180 points
- **Swing Phase**: 120 points

## 👤 Subject Information

- **Subjects**: Abesh, Adarsh, Utkarsh
- **Age Range**: 21–23 years
- **Gender**: Male
- **Height**: 165–175 cm
- **Weight**: 60–75 kg

## 🧠 Analysis Logic

- **ZMP** is calculated based on ground reaction force simulation from gait kinematics.
- **COM trajectory** is derived from joint angles and estimated mass distribution.
- **Stability Zone** ensures that COM remains within the ZMP region, ensuring safe locomotion.

## 📦 How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/cyclogram_plot.git
   cd cyclogram_plot
