from flask import Blueprint, request, jsonify
from datetime import datetime
import pytz

timezone_bp = Blueprint('timezone', __name__, url_prefix='/api')

@timezone_bp.route('/timezones', methods=['GET'])
def get_all_timezones():
    """Get all available timezones"""
    timezones = pytz.all_timezones
    return jsonify({
        'timezones': timezones,
        'count': len(timezones)
    })

@timezone_bp.route('/convert', methods=['POST'])
def convert_timezone():
    """Convert time from one timezone to another"""
    try:
        data = request.json
        
        # Validate required fields
        if not all(key in data for key in ['datetime', 'from_tz', 'to_tz']):
            return jsonify({'error': 'Missing required fields'}), 400
        
        datetime_str = data['datetime']
        from_tz = data['from_tz']
        to_tz = data['to_tz']
        
        # Parse the datetime
        dt = datetime.fromisoformat(datetime_str)
        
        # Localize to source timezone
        source_tz = pytz.timezone(from_tz)
        localized_dt = source_tz.localize(dt)
        
        # Convert to target timezone
        target_tz = pytz.timezone(to_tz)
        converted_dt = localized_dt.astimezone(target_tz)
        
        # Calculate time difference
        time_diff = (converted_dt.utcoffset() - localized_dt.utcoffset()).total_seconds() / 3600
        
        return jsonify({
            'success': True,
            'original': {
                'datetime': localized_dt.isoformat(),
                'timezone': from_tz,
                'offset': str(localized_dt.strftime('%z'))
            },
            'converted': {
                'datetime': converted_dt.isoformat(),
                'timezone': to_tz,
                'offset': str(converted_dt.strftime('%z'))
            },
            'time_difference_hours': time_diff
        })
    except ValueError as e:
        return jsonify({'error': f'Invalid datetime format: {str(e)}'}), 400
    except pytz.exceptions.UnknownTimeZoneError as e:
        return jsonify({'error': f'Unknown timezone: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@timezone_bp.route('/current', methods=['POST'])
def get_current_time():
    """Get current time in specified timezone"""
    try:
        data = request.json
        
        if 'timezone' not in data:
            return jsonify({'error': 'Missing timezone'}), 400
        
        tz = pytz.timezone(data['timezone'])
        current_time = datetime.now(tz)
        
        return jsonify({
            'success': True,
            'timezone': data['timezone'],
            'current_time': current_time.isoformat(),
            'offset': str(current_time.strftime('%z')),
            'formatted': current_time.strftime('%Y-%m-%d %H:%M:%S %Z')
        })
    except pytz.exceptions.UnknownTimeZoneError as e:
        return jsonify({'error': f'Unknown timezone: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@timezone_bp.route('/compare', methods=['POST'])
def compare_timezones():
    """Compare current time across multiple timezones"""
    try:
        data = request.json
        
        if 'timezones' not in data or not isinstance(data['timezones'], list):
            return jsonify({'error': 'Missing or invalid timezones list'}), 400
        
        comparison = []
        for tz_name in data['timezones']:
            try:
                tz = pytz.timezone(tz_name)
                current_time = datetime.now(tz)
                comparison.append({
                    'timezone': tz_name,
                    'current_time': current_time.isoformat(),
                    'formatted': current_time.strftime('%Y-%m-%d %H:%M:%S %Z'),
                    'offset': str(current_time.strftime('%z'))
                })
            except pytz.exceptions.UnknownTimeZoneError:
                comparison.append({
                    'timezone': tz_name,
                    'error': 'Unknown timezone'
                })
        
        return jsonify({
            'success': True,
            'comparison': comparison
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500
