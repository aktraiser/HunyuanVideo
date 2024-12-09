base_prompt_template = """{{mode}} mode - Video Generation Description Task:

You are a specialized AI assistant for video generation. Your task is to enhance and standardize the input description into a detailed video prompt.

Guidelines for video prompt enhancement:
1. TRANSLATION & LANGUAGE:
   - Translate any non-English input to English
   - Maintain technical terms and style-specific vocabulary

2. VISUAL ELEMENTS:
   - Specify camera angles (e.g., close-up, wide shot, tracking shot)
   - Define lighting conditions (e.g., natural daylight, golden hour, studio lighting)
   - Include atmosphere and mood descriptors
   - Describe motion and transitions

3. TECHNICAL SPECIFICATIONS:
   - Consider aspect ratio ({width}x{height})
   - Account for video duration ({duration} frames)
   - Maintain consistency across the sequence

4. STYLE AND QUALITY:
   - Specify visual style (e.g., realistic, cinematic, animated)
   - Include quality descriptors (e.g., high-definition, professional quality)
   - Define color palette or tone if relevant

5. TEMPORAL FLOW:
   - Describe the sequence of actions/events
   - Specify timing and pacing
   - Include any transitions or scene changes

Original Input: "{input}"

Please provide a comprehensive, well-structured video generation prompt that incorporates these elements while maintaining the core intention of the original input.
"""

def get_rewrite_prompt(ori_prompt, mode="Normal", width=1280, height=720, duration=129):
    """
    Generate a comprehensive video generation prompt.
    
    Args:
        ori_prompt (str): Original prompt to be enhanced
        mode (str): Mode of operation ("Normal" or "Master")
        width (int): Video width in pixels
        height (int): Video height in pixels
        duration (int): Number of frames
        
    Returns:
        str: Formatted comprehensive prompt for video generation
    """
    if mode not in ["Normal", "Master"]:
        raise ValueError(f"Mode must be 'Normal' or 'Master', got: {mode}")
        
    return base_prompt_template.format(
        mode=mode,
        input=ori_prompt,
        width=width,
        height=height,
        duration=duration
    )

# Example usage:
if __name__ == "__main__":
    ori_prompt = "一只小狗在草地上奔跑。"
    # For 720p video
    normal_prompt = get_rewrite_prompt(
        ori_prompt,
        mode="Normal",
        width=1280,
        height=720,
        duration=129
    )
    
    # For vertical video
    vertical_prompt = get_rewrite_prompt(
        ori_prompt,
        mode="Normal",
        width=720,
        height=1280,
        duration=129
    )
