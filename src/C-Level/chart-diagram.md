---
title: Chart Diagram — PlantUML Official Documentation
source: https://plantuml.com/chart-diagram
description: Official documentation for PlantUML Chart Diagram
---

# Chart Diagram

## Simple Example

```plantuml
@startchart
h-axis [Q1, Q2, Q3, Q4]
v-axis "Revenue" 0 --> 100
bar "Sales" [45, 62, 58, 70] #3498db
legend right
@endchart
```

## Bar Chart

```plantuml
@startchart
h-axis [Jan, Feb, Mar, Apr]
v-axis 0 --> 100
bar "Revenue" [45, 62, 58, 70] #1f77b4
legend right
@endchart
```

## Grouped Bars

```plantuml
@startchart
h-axis [Q1, Q2, Q3, Q4]
v-axis 0 --> 100
stackMode grouped
bar "Revenue" [45, 62, 58, 70] #3498db
bar "Profit" [35, 48, 52, 61] #2ecc71
legend right
@endchart
```

## Stacked Bars

```plantuml
@startchart
h-axis [Q1, Q2, Q3, Q4]
v-axis 0 --> 100
stackMode stacked
bar "Revenue" [45, 62, 58, 70] #3498db
bar "Costs" [25, 30, 28, 32] #e74c3c
legend right
@endchart
```

## Horizontal Bars

```plantuml
@startchart
orientation horizontal
v-axis [Product A, Product B, Product C]
h-axis "Revenue" 0 --> 100
bar [75, 55, 30] #3498db
@endchart
```

## Line Chart

```plantuml
@startchart
h-axis [Q1, Q2, Q3, Q4, Q5, Q6]
v-axis "Performance" 0 --> 100 spacing 20
line "Sales" [45, 62, 58, 70, 83, 78] #1f77b4
line "Target" [50, 55, 60, 65, 70, 75] #ff7f0e
legend right
@endchart
```

### Coordinate-Pair Notation

- Only supported for line and scatter chart types
- Requires numeric h-axis with explicit range (e.g., h-axis "x" -5 --> 5 )
- NOT compatible with categorical h-axis (e.g., h-axis [Q1, Q2, Q3, Q4] )
- All series in a chart must use the same format (either all coordinate pairs or all index-based)
- X-coordinates must fall within the h-axis range

```plantuml
@startchart
h-axis "t" -10 --> 10 spacing 2 label-right
v-axis "f(t)" -10 --> 50 spacing 10 label-top
line "Trajectory" [(-10,0), (2,10), (5,30), (8,45), (10,50)] #3498db
scatter "Checkpoints" [(1,12), (6,34), (7,47)] #e74c3c
legend right
@endchart
```

- Line charts connect points with straight line segments
- Scatter charts display individual markers at each coordinate
- Points can be unevenly spaced along the x-axis
- Gaps between points are left empty (no interpolation)

## Area Chart

```plantuml
@startchart
h-axis [Jan, Feb, Mar, Apr, May, Jun]
v-axis 0 --> 140 spacing 20
area "Product A" [45, 62, 58, 70, 83, 78] #3498db
area "Product B" [25, 35, 42, 38, 45, 40] #2ecc71
legend right
@endchart
```

## Scatter Chart

```plantuml
@startchart
<style>
.datapoints {
MarkerColor #1f77b4
MarkerShape circle
MarkerSize 10
}
.highlights {
MarkerColor #e74c3c
MarkerShape triangle
MarkerSize 10
}
</style>
h-axis [Q1, Q2, Q3, Q4, Q5]
v-axis 0 --> 100
scatter <<datapoints>> "Data Points" [20, 40, 60, 80, 70]
scatter <<highlights>> "Highlights" [30, 55, 65, 75, 85]
legend right
@endchart
```

- circle (default)
- square
- triangle

## Axes Configuration

### Horizontal Axis

```plantuml
@startchart
h-axis "Quarters" [Q1, Q2, Q3, Q4]
v-axis 0 --> 100
bar [45, 62, 58, 70] #3498db
@endchart
```

```plantuml
@startchart
orientation horizontal
v-axis [Product A, Product B, Product C]
h-axis "Revenue" 0 --> 100
bar [45, 62, 58] #3498db
@endchart
```

```plantuml
@startchart
h-axis [Jan, Feb, Mar, Apr, May, Jun] spacing 2
v-axis 0 --> 100
bar [45, 62, 58, 70, 83, 78] #3498db
@endchart
```

### Vertical Axis

```plantuml
@startchart
h-axis [Q1, Q2, Q3, Q4]
v-axis "Revenue ($M)" 0 --> 100
bar [45, 62, 58, 70] #3498db
@endchart
```

```plantuml
@startchart
title Performance
h-axis [Q1, Q2, Q3, Q4]
v-axis 0 --> 100 ticks [0:"Poor", 50:"Average", 100:"Excellent"]
bar [30, 60, 85, 95] #3498db
@endchart
```

```plantuml
@startchart
h-axis [Q1, Q2, Q3, Q4]
v-axis "Revenue ($K)" 0 --> 100 spacing 25
bar [45, 62, 58, 70] #3498db
@endchart
```

```plantuml
@startchart
h-axis [Q1, Q2, Q3, Q4]
v-axis "Profit/Loss ($K)" -50 --> 50 spacing 25
bar "Product A" [-20, 10, 30, 25] #3498db
@endchart
```

### Secondary Y-Axis

```plantuml
@startchart
h-axis [Q1, Q2, Q3, Q4]
v-axis "Revenue" 0 --> 100
v2-axis "Market Share %" 0 --> 50
bar "Sales" [45, 62, 58, 70]
line "Market Share" [15, 20, 18, 25] v2
@endchart
```

### Axis Label Positioning

- V-axis labels: vertically along the left side (reading bottom-to-top)
- V2-axis labels: vertically along the right side (reading top-to-bottom)
- H-axis labels: horizontally below the axis (centered)

#### V-Axis with label-top

```plantuml
@startchart
h-axis [Q1, Q2, Q3, Q4]
v-axis "Revenue ($K)" 0 --> 100 label-top
bar "Sales" [45, 62, 58, 70] #3498db
@endchart
```

#### H-Axis with label-right

```plantuml
@startchart
h-axis "Quarters" [Q1, Q2, Q3, Q4] label-right
v-axis "Revenue ($K)" 0 --> 100
bar "Sales" [45, 62, 58, 70] #3498db
@endchart
```

#### Combined Label Positioning

```plantuml
@startchart combined-label-positioning
h-axis "   Time" [Q1, Q2, Q3, Q4] label-right
v-axis "Revenue" 0 --> 100 label-top
v2-axis "Profit" 0 --> 50 label-top
bar "Revenue" [40, 60, 75, 90]
line "Profit" [10, 20, 30, 40] v2
legend right
@endchart
```

## Data Series Options

### Series Name

```plantuml
@startchart
h-axis [Q1, Q2, Q3, Q4]
v-axis 0 --> 100
bar "Revenue" [45, 62, 58, 70]
legend right
@endchart
```

### Colors

```plantuml
@startchart
h-axis [Q1, Q2, Q3, Q4]
v-axis 0 --> 100
bar "Series 1" [45, 62, 58, 70] #3498db
bar "Series 2" [35, 48, 52, 61] #2ecc71
bar "Series 3" [25, 30, 28, 32] #red
legend right
@endchart
```

### Data Labels

```plantuml
@startchart
h-axis [Q1, Q2, Q3, Q4]
v-axis 0 --> 100
bar "Sales" [45, 62, 58, 70] #3498db labels
line "Target" [70, 75, 80, 85] #ff7f0e labels
legend right
@endchart
```

## Layout Options

### Legend

```plantuml
@startchart
h-axis [Q1, Q2, Q3, Q4]
v-axis 0 --> 100
bar "Revenue" [45, 62, 58, 70] #3498db
bar "Profit" [35, 48, 52, 61] #2ecc71
legend right
@endchart
```

- left - Left side of chart
- right - Right side of chart
- top - Top of chart
- bottom - Bottom of chart

### Grid Lines

```plantuml
@startchart
h-axis [Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct] grid
v-axis 0 --> 100 grid
line [45, 62, 58, 70, 83, 78, 65, 72, 80, 85] #3498db
@endchart
```

```plantuml
@startchart
h-axis 0 --> 100
v-axis 0 --> 100 grid
scatter [(10,45), (25,62), (40,58), (55,70)] #3498db
@endchart
```

```plantuml
@startchart
h-axis [Q1, Q2, Q3, Q4]
v-axis 0 --> 100 grid
bar [45, 62, 58, 70] #3498db
@endchart
```

- h-axis - Enable horizontal axis gridlines (vertical lines)
- v-axis or v2-axis - Enable vertical axis gridlines (horizontal lines)
- Major gridlines only are displayed

## Annotations

```plantuml
@startchart
h-axis [Q1, Q2, Q3, Q4, Q5]
v-axis 0 --> 100
bar "Sales" [45, 62, 58, 70, 83] #3498db
line "Target" [50, 55, 60, 65, 70] #ff7f0e
annotation "Peak sales" at (Q5, 83) <<arrow>>
annotation "Target line" at (Q3, 60)
legend right
@endchart
```

- Text label
- Position coordinates (x, y)
- Optional <<arrow>> pointing to the data point

## Styling

### Inline Styling
```
bar "Revenue" [45, 62, 58, 70] #3498db
line "Target" [50, 55, 60, 65] #e74c3c
```

### Style Blocks

```plantuml
@startchart
<style>
chartDiagram {
    BackGroundColor white
    FontName Arial
    FontSize 12
    bar {
        LineColor #2c3e50
        LineThickness 2.0
        BackGroundColor #3498db
        BarWidth 0.7
    }
    line {
        LineColor #e74c3c
        LineThickness 2.5
    }
    scatter {
        MarkerShape square
        MarkerSize 14
        MarkerColor #9b59b6
    }
    axis {
        LineColor #34495e
        LineThickness 1.5
        FontSize 11
        FontColor #7f8c8d
    }
    grid {
        LineColor #ecf0f1
        LineThickness 0.8
    }
    legend {
        FontSize 12
        FontColor #2c3e50
        BackGroundColor #f5f5f5
        Padding 10
        Margin 5
    }
}
</style>
@endchart
```
