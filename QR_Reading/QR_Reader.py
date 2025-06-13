#!/usr/bin/env python3
"""
Enhanced QR Code Scanner
Combines real-time QR code detection using OpenCV with support for both webcam and drone applications.
Supports both pyzbar and OpenCV's built-in QR detector for maximum compatibility.
"""

import cv2
import numpy as np
import sys
import datetime
import argparse
from pathlib import Path

# Try to import pyzbar for enhanced QR detection
try:
    from pyzbar import pyzbar
    PYZBAR_AVAILABLE = True
    print("✅ Pyzbar available - Enhanced QR detection enabled")
except ImportError:
    PYZBAR_AVAILABLE = False
    print("⚠️  Pyzbar not available - Using OpenCV QR detector only")
    print("Install pyzbar for better detection: pip install pyzbar")

class QRCodeScanner:
    """Enhanced QR Code Scanner supporting multiple detection methods and input sources."""
    
    def __init__(self, source=0, continuous=True, save_log=False, display_on_frame=True):
        """
        Initialize QR Code Scanner
        
        Args:
            source: Video source (0 for webcam, URL for streams)
            continuous: Continue scanning after first detection
            save_log: Save detected QR codes to log file
            display_on_frame: Display QR text on video frame
        """
        self.source = source
        self.continuous = continuous
        self.save_log = save_log
        self.display_on_frame = display_on_frame
        self.qr_detector = cv2.QRCodeDetector()
        self.log_file = "qr_scan_log.txt"
        
        # Initialize video capture
        self.cap = cv2.VideoCapture(source)
        if not self.cap.isOpened():
            raise RuntimeError(f"❌ Failed to open video source: {source}")
        
        # Optimize capture settings
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
        self.cap.set(cv2.CAP_PROP_FPS, 30)
        
        print("🎥 Video capture initialized successfully")
        
    def detect_qr_pyzbar(self, frame):
        """Detect QR codes using pyzbar library."""
        if not PYZBAR_AVAILABLE:
            return []
        
        try:
            qr_codes = pyzbar.decode(frame)
            results = []
            
            for qr_code in qr_codes:
                # Extract QR code data and position
                data = qr_code.data.decode('utf-8')
                rect = qr_code.rect
                polygon = qr_code.polygon
                
                # Convert polygon points for drawing
                points = [(point.x, point.y) for point in polygon]
                
                results.append({
                    'data': data,
                    'rect': (rect.left, rect.top, rect.width, rect.height),
                    'points': points,
                    'method': 'pyzbar'
                })
        except Exception as e:
            print(f"⚠️  Pyzbar detection error: {e}")
        
        return results
    
    def detect_qr_opencv(self, frame):
        """Detect QR codes using OpenCV's built-in detector."""
        try:
            data, points, _ = self.qr_detector.detectAndDecode(frame)
            results = []
            
            if data and points is not None and len(points) > 0:
                # Convert points to integer coordinates
                points = points[0].astype(int)
                
                # Calculate bounding rectangle
                x, y, w, h = cv2.boundingRect(points)
                
                results.append({
                    'data': data,
                    'rect': (x, y, w, h),
                    'points': points.tolist(),
                    'method': 'opencv'
                })
        except Exception as e:
            print(f"⚠️  OpenCV detection error: {e}")
        
        return results
    
    def draw_qr_detection(self, frame, qr_result):
        """Draw QR code detection on frame."""
        data = qr_result['data']
        rect = qr_result['rect']
        points = qr_result['points']
        method = qr_result['method']
        
        # Draw bounding box
        x, y, w, h = rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
        
        # Draw polygon outline if available
        if len(points) > 2:
            if method == 'pyzbar':
                pts = [(int(p[0]), int(p[1])) for p in points]
            else:
                pts = [(int(p[0]), int(p[1])) for p in points]
            
            cv2.polylines(frame, [np.array(pts, np.int32)], True, (0, 255, 0), 2)
        
        # Display QR data on frame
        if self.display_on_frame:
            # Prepare text display
            text_lines = [f"QR Code ({method}):", data[:50] + "..." if len(data) > 50 else data]
            
            # Calculate text position
            text_y = max(30, y - 10)
            
            for i, line in enumerate(text_lines):
                text_pos = (x, text_y + i * 25)
                
                # Draw text background
                (text_w, text_h), _ = cv2.getTextSize(line, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 2)
                cv2.rectangle(frame, (text_pos[0] - 5, text_pos[1] - text_h - 5), 
                            (text_pos[0] + text_w + 5, text_pos[1] + 5), (0, 0, 0), -1)
                
                # Draw text
                cv2.putText(frame, line, text_pos, cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
    
    def log_qr_detection(self, data, method):
        """Log QR detection to file."""
        if not self.save_log:
            return
        
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"{timestamp} | {method} | {data}\n"
        
        try:
            with open(self.log_file, "a", encoding="utf-8") as f:
                f.write(log_entry)
            print(f"📝 Logged to {self.log_file}")
        except Exception as e:
            print(f"❌ Failed to write log: {e}")
    
    def run(self):
        """Main scanning loop."""
        print("🚀 QR Code Scanner started!")
        print("Controls:")
        print("  - Press 'q' or ESC to quit")
        print("  - Press 's' to save current frame")
        print("  - Press 'p' to pause/resume")
        
        paused = False
        frame_count = 0
        
        try:
            while True:
                if not paused:
                    ret, frame = self.cap.read()
                    if not ret:
                        print("❌ Failed to grab frame - retrying...")
                        continue
                    
                    frame_count += 1
                    original_frame = frame.copy()
                
                # Try both detection methods
                qr_results = []
                
                # Method 1: Pyzbar (if available)
                if PYZBAR_AVAILABLE:
                    qr_results.extend(self.detect_qr_pyzbar(frame))
                
                # Method 2: OpenCV (if no pyzbar results or as backup)
                if not qr_results:
                    qr_results.extend(self.detect_qr_opencv(frame))
                
                # Process detected QR codes
                for qr_result in qr_results:
                    data = qr_result['data']
                    method = qr_result['method']
                    
                    print(f"🎯 QR Code detected ({method}): {data}")
                    
                    # Draw detection on frame
                    self.draw_qr_detection(frame, qr_result)
                    
                    # Log detection
                    self.log_qr_detection(data, method)
                    
                    # Exit after first detection if not continuous
                    if not self.continuous:
                        print("✅ Detection complete. Exiting...")
                        cv2.imshow('QR Code Scanner', frame)
                        cv2.waitKey(2000)  # Show result for 2 seconds
                        return
                
                # Add status information to frame
                status_text = f"Frame: {frame_count} | Mode: {'Continuous' if self.continuous else 'Single'}"
                if paused:
                    status_text += " | PAUSED"
                
                cv2.putText(frame, status_text, (10, frame.shape[0] - 10), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
                
                # Display frame
                cv2.imshow('QR Code Scanner', frame)
                
                # Handle key presses
                key = cv2.waitKey(1) & 0xFF
                if key == ord('q') or key == 27:  # 'q' or ESC
                    break
                elif key == ord('s'):  # Save frame
                    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                    filename = f"qr_scan_{timestamp}.jpg"
                    cv2.imwrite(filename, original_frame)
                    print(f"💾 Frame saved as {filename}")
                elif key == ord('p'):  # Pause/resume
                    paused = not paused
                    print(f"⏸️  {'Paused' if paused else 'Resumed'}")
        
        except KeyboardInterrupt:
            print("\n⏹️  Interrupted by user")
        except Exception as e:
            print(f"❌ Error during scanning: {e}")
        finally:
            self.cleanup()
    
    def cleanup(self):
        """Clean up resources."""
        print("🧹 Cleaning up...")
        self.cap.release()
        cv2.destroyAllWindows()
        print("✅ Cleanup complete")

def main():
    """Main function with command-line argument parsing."""
    parser = argparse.ArgumentParser(description="Enhanced QR Code Scanner")
    parser.add_argument("--source", "-s", default=0, 
                       help="Video source (0 for webcam, URL for streams)")
    parser.add_argument("--continuous", "-c", action="store_true", default=True,
                       help="Continue scanning after first detection")
    parser.add_argument("--single", action="store_true",
                       help="Exit after first QR code detection")
    parser.add_argument("--log", "-l", action="store_true",
                       help="Save detected QR codes to log file")
    parser.add_argument("--no-display", action="store_true",
                       help="Don't display QR text on video frame")
    
    args = parser.parse_args()
    
    # Handle source conversion
    source = args.source
    if source != 0:
        try:
            source = int(source)  # Try to convert to integer for camera index
        except ValueError:
            pass  # Keep as string for URL/path
    
    try:
        scanner = QRCodeScanner(
            source=source,
            continuous=not args.single,
            save_log=args.log,
            display_on_frame=not args.no_display
        )
        scanner.run()
    except Exception as e:
        print(f"❌ Scanner initialization failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
