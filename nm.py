<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Camerade</class>
 <widget class="QMainWindow" name="Camerade">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>1525</width>
    <height>730</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <property name="styleSheet">
   <string notr="true">QWidget#centralwidget{background-color: rgb(17, 17, 17);}</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <property name="styleSheet">
    <string notr="true">background-color:rgb(26, 26, 26)</string>
   </property>
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>90</y>
      <width>640</width>
      <height>480</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(255,255,255);</string>
    </property>
    <property name="frameShadow">
     <enum>QFrame::Plain</enum>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>580</y>
      <width>191</width>
      <height>51</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <italic>true</italic>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">broder-radius:100px;
background-color:rgb(0,128,0);
</string>
    </property>
    <property name="text">
     <string>Start</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_2">
    <property name="geometry">
     <rect>
      <x>230</x>
      <y>580</y>
      <width>201</width>
      <height>51</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">broder-radius:100px;
background-color:rgb(128,0,0);</string>
    </property>
    <property name="text">
     <string>Stop</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_3">
    <property name="geometry">
     <rect>
      <x>450</x>
      <y>580</y>
      <width>211</width>
      <height>51</height>
     </rect>
    </property>
    <property name="autoFillBackground">
     <bool>false</bool>
    </property>
    <property name="styleSheet">
     <string notr="true">
broder-radius:200000px;
background-color:rgb(50,50,50);
</string>
    </property>
    <property name="text">
     <string>Exit</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>20</y>
      <width>561</width>
      <height>41</height>
     </rect>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QLCDNumber" name="lcdNumber">
    <property name="geometry">
     <rect>
      <x>690</x>
      <y>60</y>
      <width>111</width>
      <height>51</height>
     </rect>
    </property>
   </widget>
   <widget class="QLCDNumber" name="lcdNumber_2">
    <property name="geometry">
     <rect>
      <x>690</x>
      <y>140</y>
      <width>111</width>
      <height>41</height>
     </rect>
    </property>
   </widget>
   <widget class="QLCDNumber" name="lcdNumber_3">
    <property name="geometry">
     <rect>
      <x>690</x>
      <y>270</y>
      <width>111</width>
      <height>51</height>
     </rect>
    </property>
   </widget>
   <widget class="QLCDNumber" name="lcdNumber_4">
    <property name="geometry">
     <rect>
      <x>690</x>
      <y>210</y>
      <width>111</width>
      <height>41</height>
     </rect>
    </property>
   </widget>
   <widget class="QLCDNumber" name="lcdNumber_5">
    <property name="geometry">
     <rect>
      <x>690</x>
      <y>450</y>
      <width>121</width>
      <height>41</height>
     </rect>
    </property>
   </widget>
   <widget class="QLCDNumber" name="lcdNumber_6">
    <property name="geometry">
     <rect>
      <x>700</x>
      <y>350</y>
      <width>111</width>
      <height>51</height>
     </rect>
    </property>
   </widget>
   <widget class="QLCDNumber" name="lcdNumber_7">
    <property name="geometry">
     <rect>
      <x>690</x>
      <y>590</y>
      <width>121</width>
      <height>41</height>
     </rect>
    </property>
   </widget>
   <widget class="QLCDNumber" name="lcdNumber_8">
    <property name="geometry">
     <rect>
      <x>690</x>
      <y>520</y>
      <width>121</width>
      <height>41</height>
     </rect>
    </property>
   </widget>
   <widget class="QGraphicsView" name="graphicsView">
    <property name="geometry">
     <rect>
      <x>1220</x>
      <y>210</y>
      <width>256</width>
      <height>192</height>
     </rect>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_4">
    <property name="geometry">
     <rect>
      <x>1020</x>
      <y>580</y>
      <width>181</width>
      <height>71</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">broder-radius:100px;
background-color:rgb(0,128,0);</string>
    </property>
    <property name="text">
     <string>Start time</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_5">
    <property name="geometry">
     <rect>
      <x>1290</x>
      <y>580</y>
      <width>171</width>
      <height>71</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">broder-radius:200px;
background-color:rgb(50,50,50);</string>
    </property>
    <property name="text">
     <string>Reset</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_6">
    <property name="geometry">
     <rect>
      <x>1200</x>
      <y>20</y>
      <width>151</width>
      <height>61</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">QPushButton{
background-color: rgb(6, 47, 91);
}</string>
    </property>
    <property name="text">
     <string>Map / location</string>
    </property>
   </widget>
   <widget class="QDial" name="dial">
    <property name="geometry">
     <rect>
      <x>850</x>
      <y>60</y>
      <width>50</width>
      <height>64</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">QDial{
qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.077, fx:0.5, fy:0.5, stop:0 rgba(0, 169, 255, 147), stop:0.497326 rgba(0, 0, 0, 147), stop:1 rgba(0, 169, 255, 147))

}</string>
    </property>
   </widget>
   <widget class="QDial" name="dial_2">
    <property name="geometry">
     <rect>
      <x>850</x>
      <y>130</y>
      <width>50</width>
      <height>64</height>
     </rect>
    </property>
   </widget>
   <widget class="QDial" name="dial_3">
    <property name="geometry">
     <rect>
      <x>850</x>
      <y>200</y>
      <width>50</width>
      <height>64</height>
     </rect>
    </property>
   </widget>
   <widget class="QDial" name="dial_4">
    <property name="geometry">
     <rect>
      <x>850</x>
      <y>270</y>
      <width>50</width>
      <height>64</height>
     </rect>
    </property>
   </widget>
   <widget class="QDial" name="dial_5">
    <property name="geometry">
     <rect>
      <x>850</x>
      <y>340</y>
      <width>50</width>
      <height>64</height>
     </rect>
    </property>
   </widget>
   <widget class="QDial" name="dial_6">
    <property name="geometry">
     <rect>
      <x>850</x>
      <y>430</y>
      <width>50</width>
      <height>64</height>
     </rect>
    </property>
   </widget>
   <widget class="QDial" name="dial_7">
    <property name="geometry">
     <rect>
      <x>850</x>
      <y>510</y>
      <width>50</width>
      <height>64</height>
     </rect>
    </property>
   </widget>
   <widget class="QDial" name="dial_8">
    <property name="geometry">
     <rect>
      <x>850</x>
      <y>580</y>
      <width>50</width>
      <height>64</height>
     </rect>
    </property>
   </widget>
   <widget class="QLCDNumber" name="lcdNumber_9">
    <property name="geometry">
     <rect>
      <x>1010</x>
      <y>430</y>
      <width>441</width>
      <height>121</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">QLCDNumber{
background-color: darkgreen;

}</string>
    </property>
   </widget>
   <widget class="QLCDNumber" name="lcdNumber_10">
    <property name="geometry">
     <rect>
      <x>980</x>
      <y>110</y>
      <width>491</width>
      <height>81</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">QLCDNumber{
background-color: darkgreen;

}</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>1525</width>
     <height>25</height>
    </rect>
   </property>
   <widget class="QMenu" name="menuDark_mode">
    <property name="title">
     <string>Dark mode</string>
    </property>
   </widget>
   <addaction name="menuDark_mode"/>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>