from django.shortcuts import render, redirect
import requests
import random
from django.http import HttpResponse, HttpResponseRedirect
from difflib import SequenceMatcher


def main_page(request):
    return render(request, 'football_app/main_page.html')



def choose_team(request):
    max_retries = 100000  
    retries = 0
    guessed_count = request.session.get('guessed_count',0)
   
    user_input = request.POST.get('user_input', '')
    team_name = request.session.get('team_name','No team name')
    if user_input:
        if user_input.lower() == team_name.lower():
            guessed_count += 1
            request.session['guessed_count'] = guessed_count  
        else:
            request.session['guessed_count'] = 0
            request.session['team_name'] = ''
            return redirect('game_over', guessed_count=guessed_count)
            
 
    while retries < max_retries:
        team_id = random.randint(1, 3000)
        api_url = f'http://api.football-data.org/v4/teams/{team_id}'
        headers = {'X-Auth-Token': '58673914aa9c44c6a9cfd800ded4ae91'} 
        response = requests.get(api_url, headers=headers)
        if response.status_code == 200:
            team = response.json()
            team_name = team.get('name', 'No Team Name')
            team_logo_url = team.get('crest', '')
            print(team_name)
            request.session['team_name'] = team_name
 
            return render(request, 'football_app/choose_team.html', {
                'team_logo_url': team_logo_url,
                'guessed_count': guessed_count,
                'team_name': team_name,  
            })
 
       
        print(f'Failed to fetch team data. Status code: {response.status_code}')
 
        retries += 1
 
    return HttpResponse('Failed to fetch team data after several retries')



def game_over(request, guessed_count):
    return render(request, 'football_app/game_over.html', {'guessed_count': guessed_count})




